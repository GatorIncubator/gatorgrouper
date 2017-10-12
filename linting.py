"""
run with `pytest linting.py`
This will get moved to the test suite when it is completed.
Requires
"""

import pytest
import glob
from flake8.api import legacy as flake8

def test_1():
    assert True

    filenames = glob.glob('gatorgrouper/*.py')
    style_guide = flake8.get_style_guide(ignore=['E24', 'W503'])
    report = style_guide.check_files(filenames)
    assert report.get_statistics('E') == [], 'Flake8 found violations'
