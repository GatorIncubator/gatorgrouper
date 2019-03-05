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


@pytest.fixture(scope="session")
def generate_csv_no_header(tmpdir_factory):
    """ Generate a tempory sample csv """
    fn = tmpdir_factory.mktemp("data").join("csvNg.csv")
    with open(str(fn), "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [["delgrecoj", True, True, False, True], ["delgrecoj2", True, True, False, True]]
        )
    csvfile.close()
    return str(fn)


def test_read_student_file(generate_csv):
    """ Test read_student_file """
    expectedoutput = [["delgrecoj", True, True, False, True]]
    assert read_student_file.read_csv_data(generate_csv) == expectedoutput


def test_read_student_file_no_header(generate_csv_no_header):
    """ Test read_student_file """
    expectedoutput = [["delgrecoj", True, True, False, True], ["delgrecoj2", True, True, False, True]]
    assert read_student_file.read_csv_data(generate_csv_no_header) == expectedoutput
