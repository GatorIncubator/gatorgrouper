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
def generate_csv_preference(tmpdir_factory):
    """ Generate a tempory sample csv """
    fn = tmpdir_factory.mktemp("data").join("csvNgp.csv")
    headers = ["NAME", "NAME2"]
    with open(str(fn), "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerow({"NAME": "delgrecoj", "NAME2": "delgrecoj2"})
        writer.writerow({"NAME": "delgrecoj2", "NAME2": "delgrecoj"})
        writer.writerow({"NAME": "delgrecoj3", "NAME2": "delgrecoj4"})
        writer.writerow({"NAME": "delgrecoj4", "NAME2": "delgrecoj3"})
        writer.writerow({"NAME": "delgrecoj5", "NAME2": "delgrecoj6"})
        writer.writerow({"NAME": "delgrecoj6", "NAME2": "delgrecoj5"})
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
    headers = ["NAME", "Q1", "Q2", "Q3", "Q4", "Q5"]
    with open(str(fn), "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerow(
            {
                "NAME": "delgrecoj",
                "Q1": "1.2",
                "Q2": "1.1",
                "Q3": "0.9",
                "Q4": "2.3",
                "Q5": "Name",
            }
        )
    return str(fn)


@pytest.fixture(scope="session")
def generate_csv_float_no_header(tmpdir_factory):
    """ Generate a tempory sample csv """
    fn = tmpdir_factory.mktemp("data").join("csvNg1.csv")
    data = [
        # optionally include headers as the first entry
        ["delgrecoj", "1.2", "0.7", "1.1", "0.2", "Name"],
        ["delgrecoj2", "0.1", "0.5", "0.8", "0.6", "Name"],
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


@pytest.fixture(scope="session")
def generate_csv_file(tmpdir_factory):
    """ Generate a sample csv file that returns the file object """
    fn = tmpdir_factory.mktemp("data").join("csvNg.csv")
    headers = ["NAME", "Q1", "Q2", "Q3", "Q4"]
    with open(str(fn), "w", encoding="utf-8") as csvfile:
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
    return fn
