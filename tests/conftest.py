"""Configuration file for the test suite"""
import os
import sys
import csv

import pytest

# set the system path to contain the previous directory
# the utils folder must be in the PYTHONPATH
MYPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MYPATH + "/gatorgrouper/utils/")


@pytest.fixture(scope="session")
def generate_csv(tmpdir_factory):
    """ Generate a tempory sample csv """
    fn = tmpdir_factory.mktemp("data").join("csvNg.csv")
    headers = ["NAME", "Q1", "Q2", "Q3", "Q4"]
    with open(str(fn), "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerow(
            {
                "NAME": "delgrecoj",
                "Q1": "True",
                "Q2": "True",
                "Q3": "False",
                "Q4": "True",
            }
        )
        writer.writerow(
            {
                "NAME": "delgrecoj2",
                "Q1": "True",
                "Q2": "True",
                "Q3": "False",
                "Q4": "True",
            }
        )
        writer.writerow(
            {
                "NAME": "delgrecoj3",
                "Q1": "True",
                "Q2": "True",
                "Q3": "False",
                "Q4": "True",
            }
        )
        writer.writerow(
            {
                "NAME": "delgrecoj4",
                "Q1": "True",
                "Q2": "True",
                "Q3": "False",
                "Q4": "True",
            }
        )
        writer.writerow(
            {
                "NAME": "delgrecoj5",
                "Q1": "True",
                "Q2": "True",
                "Q3": "False",
                "Q4": "True",
            }
        )
        writer.writerow(
            {
                "NAME": "delgrecoj6",
                "Q1": "True",
                "Q2": "True",
                "Q3": "False",
                "Q4": "True",
            }
        )
    return str(fn)


@pytest.fixture(scope="session")
def generate_csv_no_header(tmpdir_factory):
    """ Generate a tempory sample csv """
    fn = tmpdir_factory.mktemp("data").join("csvNg1.csv")
    data = [
        # optionally include headers as the first entry
        ["delgrecoj", "True", "True", "False", "True"],
        ["delgrecoj2", "True", "True", "True", "True"],
    ]
    csv_string = ""
    for entry in data:
        csv_string += ",".join(entry) + "\r\n"
    with open(str(fn), "w") as csvfile:
        csvfile.write(csv_string)
    return str(fn)


@pytest.fixture(scope="session")
def generate_csv_float(tmpdir_factory):
    """ Generate a tempory sample csv """
    fn = tmpdir_factory.mktemp("data").join("csvNg.csv")
    headers = ["NAME", "Q1", "Q2", "Q3", "Q4"]
    with open(str(fn), "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerow(
            {"NAME": "delgrecoj", "Q1": "1.2", "Q2": "1.1", "Q3": "0.9", "Q4": "2.3"}
        )
    return str(fn)


@pytest.fixture(scope="session")
def generate_csv_float_no_header(tmpdir_factory):
    """ Generate a tempory sample csv """
    fn = tmpdir_factory.mktemp("data").join("csvNg1.csv")
    data = [
        # optionally include headers as the first entry
        ["delgrecoj", "1.2", "0.7", "1.1", "0.2"],
        ["delgrecoj2", "0.1", "0.5", "0.8", "0.6"],
    ]
    csv_string = ""
    for entry in data:
        csv_string += ",".join(entry) + "\r\n"
    with open(str(fn), "w") as csvfile:
        csvfile.write(csv_string)
    return str(fn)


@pytest.fixture
def no_arguments():
    """Return no command-line arguments"""
    return []
