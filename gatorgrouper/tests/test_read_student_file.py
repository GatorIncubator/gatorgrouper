""" Testing read_student_file """

import csv

# pylint: disable=redefined-outer-name
import pytest

from utils import read_student_file


@pytest.fixture(scope="session")
def generate_csv(tmpdir_factory):
    """ Generate a tempory sample csv """
    fn = tmpdir_factory.mktemp("data").join("csvNg.csv")
    headers = ["NAME", "Q1", "Q2", "Q3", "Q4"]
    with open(str(fn), "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerow(
            {"NAME": "delgrecoj", "Q1": True, "Q2": True, "Q3": False, "Q4": True}
        )
    return str(fn)


def test_read_student_file(generate_csv):
    """ Test read_student_file """
    expectedoutput = [["delgrecoj", True, True, False, True]]
    assert read_student_file.read_student_file(generate_csv) == expectedoutput
