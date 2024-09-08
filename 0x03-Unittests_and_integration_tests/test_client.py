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
from parameterized import parameterized
from client import GithubOrgClient


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


if __name__ == "__main__":
    unittest.main()
