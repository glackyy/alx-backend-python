#!/usr/bin/env python3
"""Testing the Client Module"""
import unittest
from parameterized import parameterized
from unittest.mock import (
    patch,
    MagicMock,
    Mock
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
            "http://api.github.com/orgs/{}".format(org)
        )
