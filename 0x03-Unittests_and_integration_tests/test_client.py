#!/usr/bin/env python3
""" Unittest module """
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from parameterized import parameterized


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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test that the list of repos is what you expect."""
        json_payload = [{"name": "Google"}, {"name": "Yahoo"}]
        org = "mock"
        mock_json.return_value = json_payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as repos_url:
            repos_url.return_value = 'hello/world'
            response = GithubOrgClient(org).public_repos()
            check = [i["name"] for i in json_payload]
            self.assertEqual(response, check)
            mock_json.assert_called_once()
