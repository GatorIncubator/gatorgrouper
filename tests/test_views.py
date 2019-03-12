"""Testing views"""
from django.test import RequestFactory
import pytest
from gatorgrouper import views
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse


def test_upload_csv(self):
    response = self.client.get('/')
    assert response.status_code == 200
