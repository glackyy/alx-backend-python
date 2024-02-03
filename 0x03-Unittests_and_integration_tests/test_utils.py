#!/usr/bin/env python3
"""Testing utils Module"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import(
    access_nested_map,
)

class TestAccessNestedMap(unittest.TestCase):
    """Testing the access_nested_map func"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Testing access_nested_map output"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Testing access_nested_map exception raising"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)