"""Testing settings"""
import pytest
import settings

def test_find_or_create_secret_key():
    """test if key is 50 characters"""
    key = settings.find_or_create_secret_key()
    assert len(key) == 50

def test_if_generate_random_key():
    """see if it generates a ranfom key of key is not provided"""
    settings.SECRET_KEY_DIR = None 
    settings.SECRET_KEY_FILEPATH = None
    key = settings.find_or_create_secret_key()
    assert len(key) == 50
