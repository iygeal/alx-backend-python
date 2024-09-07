#!/usr/bin/env python3
"""This method provides some test cases for utils.py"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with different inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),  # An empty map with a path trying to access key "a"
        # A map with "a", but no "b" inside "a"
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that KeyError is raised for missing keys in nested_map"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test class for get_json function"""

    @parameterized.expand([
        ("htpp://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')  # Mocking requests.get
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns expected result and calls request.get
        with the correct url
        """

        # Configure the mock to return a response with the json() method
        # returning test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function with the test URL
        result = get_json(test_url)

        # Assert that requests.get was called once with the correct URL
        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test classfor memoize decorator"""

    def test_memoize(self):
        """Test that a_property is memoized and
        a_method is called only once
        """
        class TestClass:
            """A class with memoized property for testing"""

            def a_method(self):
                """A method that returns 42"""
                return 42

            @memoize
            def a_property(self):
                """A memoized property that returns the result of a_method"""
                return self.a_method()

        # Use patch to mock TestClass.a_method
        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_a_method:
            # Create an instance of TestClass
            instance = TestClass()

            # Access a_property twice
            result1 = instance.a_property
            result2 = instance.a_property

            # Assert that a_method was called only once
            mock_a_method.assert_called_once()

            # Assert that the result of a_property is 42
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
