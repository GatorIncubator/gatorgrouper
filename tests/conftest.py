"""Configuration file for the test suite"""
import os
import sys
import csv
import pandas as pd

# pylint: disable=redefined-outer-name
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
    return str(fn)


@pytest.fixture(scope="session")
def generate_csv_no_header(tmpdir_factory):
    """ Generate a tempory sample csv """
    fn = tmpdir_factory.mktemp("data").join("csvNg1.csv")
    df_list = {
        "NAME": ["delgrecoj", "delgrecoj2"],
        "Q1": ["True", "True"],
        "Q2": ["True", "True"],
        "Q3": ["False", "True"],
        "Q4": ["True", "True"],
    }
    df = pd.DataFrame(df_list)
    df.to_csv(str(fn), index=False, header=False)
    return str(fn)


@pytest.fixture
def no_arguments():
    """Return no command-line arguments"""
    return []
