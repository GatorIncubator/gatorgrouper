"""models.py testing"""

import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestModel:
    def test_Professor(self):
        obj = mixer.blend('gatorgrouper.Professor')
        # it creates a professor instance
        assert obj.pk == 1

    def test_str(self):
        obj = mixer.blend('gatorgrouper.Professor', last_name = 'K', first_name = 'Greg')
        result = obj.__str__(self)
        expected = 'Greg K'
        assert result == expected
