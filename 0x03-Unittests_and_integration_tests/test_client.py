#!/usr/bin/env python3
""" Unittest module """

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """ Test method returns correct output """
        endpoint = 'https://api.github.com/orgs/{}'.format(org_name)
        spec = GithubOrgClient(org_name)
        spec.org()
        mock_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """ Test method returns correct output """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @parameterized.expand([
        ("random_url", {"repos_url": "https://some.com"})
    ])
    @patch('client.get_json')
    def test_public_repos(self, name, result, mock_json):
        """
        Test that the list of repos is what you expect
        from the chosen payload.
        """
        with patch('GithubOrgClient._public_repos_url',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name).public_repos()
            self.assertEqual(response, result.get('repos_url'))
            mock_json.assert_called_once()
