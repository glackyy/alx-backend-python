#!/usr/bin/env python3
"""Testing the Client Module"""
import unittest
from parameterized import parameterized
from unittest.mock import (
    patch,
    MagicMock,
    Mock,
    PropertyMock
)
from typing import Dict
from client import (
    GithubOrgClient
)


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, response: Dict, mocked: MagicMock) -> None:
        """Testing the org Method"""
        mocked.return_value = MagicMock(return_value=response)
        github_o_cl = GithubOrgClient(org)
        self.assertEqual(github_o_cl.org(), response)
        mocked.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """Testing the public_repos_url property"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mocked_org:
            mocked_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
