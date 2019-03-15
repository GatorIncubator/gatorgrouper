"""Testing settings"""
import pytest
import settings
import os


def test_find_or_create_secret_key():
    """test if key is 50 characters"""
    key = settings.find_or_create_secret_key()
    assert len(key) == 50
