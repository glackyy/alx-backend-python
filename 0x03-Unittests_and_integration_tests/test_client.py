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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Testing public_repos Method"""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart",
                    "private": False,
                    "owner": {
                    "login": "google",
                    "id": 1342004,
                    "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
                    "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/google",
                    "html_url": "https://github.com/google",
                    "followers_url": "https://api.github.com/users/google/followers",
                    "following_url": "https://api.github.com/users/google/following{/other_user}",
                    "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/google/subscriptions",
                    "organizations_url": "https://api.github.com/users/google/orgs",
                    "repos_url": "https://api.github.com/users/google/repos",
                    "events_url": "https://api.github.com/users/google/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/google/received_events",
                    "type": "Organization",
                    "site_admin": False
                    },
                
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                }
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        