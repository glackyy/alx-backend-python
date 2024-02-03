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
        