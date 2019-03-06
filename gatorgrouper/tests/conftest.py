"""Configuration file for the test suite"""
import os
import sys
import pytest


# set the system path to contain the previous directory
# the utils folder must be in the PYTHONPATH
MYPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MYPATH + "/../utils/")

@pytest.fixture(scope="session")
def generate_csv(tmpdir_factory):
    fn = tmpdir_factory.mktemp("data").join("csvNg.csv")
    headers = ["NAME", "Q1", "Q2", "Q3", "Q4"]
    with open(str(fn), "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerow(
            {"NAME": "delgrecoj", "Q1": True, "Q2": True, "Q3": False, "Q4": True}
        )
    return str(fn)
