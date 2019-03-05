""" Testing read_student_file """

import csv
import pandas as pd

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
    fn = tmpdir_factory.mktemp("data").join("csvNg1.csv")
    df_list = {
        "NAME": ["delgrecoj"],
        "Q1": [True],
        "Q2": [True],
        "Q3": [False],
        "Q4": [True],
    }
    df = pd.DataFrame(df_list)
    df.to_csv(str(fn), index=False, header=False, delimiter=",")
    return str(fn)


def test_read_student_file(generate_csv):
    """ Test read_student_file """
    expectedoutput = [["delgrecoj", True, True, False, True]]
    assert read_student_file.read_csv_data(generate_csv) == expectedoutput


def test_read_student_file_no_header(generate_csv_no_header):
    """ Test read_student_file """
    expectedoutput = []
    assert read_student_file.read_csv_data(generate_csv_no_header) == expectedoutput
