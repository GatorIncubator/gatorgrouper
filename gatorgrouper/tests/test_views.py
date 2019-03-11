"""Testing views"""
from django.test import RequestFactory
import pytest
from views import index
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse


def test_home_page_status_code(self):
    response = self.client.get('/')
    assert response.status_code == 200
