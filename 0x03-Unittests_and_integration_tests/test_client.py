#!/usr/bin/env python3
"""Test module for the client.py file
"""
import unittest
from unittest.mock import (
    patch,
    Mock,
    PropertyMock,
    MagicMock
)
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient."""

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_json, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Configure the mock to return a specific value
        mock_get_json.return_value = expected_json

        # Create an instance of GithubOrgClient with the given org_name
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Assert that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        # Assert that the returned value is as expected
        self.assertEqual(result, expected_json)

    def test_public_repos_url(self):
        """Tests the `_public_repos_url` property."""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos
        returns the correct list of repos.
        """
        # Define a mock payload returned by get_json
        mock_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "apache-2.0"}},
        ]

        # Configure the mock to return this payload
        mock_get_json.return_value = mock_repos_payload

        # Mock the _public_repos_url property to return a specific URL
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/google/repos"
        ) as mock_public_repos_url:
            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")

            # Call the public_repos method
            repos = client.public_repos()

            # Assert that the returned list of repos
            # matches the expected output
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])

            # Check that _public_repos_url was called once
            mock_public_repos_url.assert_called_once()

            # Check that get_json was called once with the correct URL
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),  # Case with missing license key
        # Case with missing key in license
        ({"license": {}}, "my_license", False),
        # Case with None as key
        ({"license": {"key": None}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos."""

    @classmethod
    def setUpClass(cls):
        """Set up the class for integration tests by patching requests.get."""
        # Start patching requests.get
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        # Define side_effect for the mock to return the appropriate fixture
        mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher after tests."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method."""
        client = GithubOrgClient("google")

        # Test that public_repos returns the expected list of repo names
        self.assertEqual(client.public_repos(), self.expected_repos)

        # Test that public_repos with a specific license
        # returns the expected repos
        self.assertEqual(client.public_repos(
            license="apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
