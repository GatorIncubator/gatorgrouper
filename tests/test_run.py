"""Testing run method"""

from gatorgrouper.utils import parse_arguments
from gatorgrouper.utils import read_student_file
from gatorgrouper.utils import run


def test_run_random_remove_absent(generate_csv):
    """ Test if the main program can run group random with absent student """
    command = ["--file", generate_csv, "--num-group", "3", "--absentees", "delgrecoj"]
    input_arguments = parse_arguments.parse_arguments(command)
    output = run.run_arguments(input_arguments)
    assert len(output) == 3


def test_run_graph(generate_csv, generate_csv_preference):
    """ Test if the main program can run group graph with preference """
    command = [
        "--file",
        generate_csv,
        "--num-group",
        "2",
        "--method",
        "graph",
        "--preferences",
        generate_csv_preference,
        "--preferences-weight",
        "1.1",
        "--preferences-weight-match",
        "1.3",
    ]
    input_arguments = parse_arguments.parse_arguments(command)
    preference = dict(read_student_file.read_csv_data(input_arguments.preferences))
    output = run.run_arguments(input_arguments, preference)
    assert len(output) == 2


def test_run_rrobin(generate_csv):
    """ Test if the main program can run rrobin"""
    command = ["--file", generate_csv, "--num-group", "3", "--method", "rrobin"]
    input_arguments = parse_arguments.parse_arguments(command)
    output = run.run_arguments(input_arguments)
    assert len(output) == 3


def test_run_rrobin_to_random():
    """ Test if the main program can run rrobin then transfer to random """
    namelist = [["A"], ["B"], ["C"], ["D"]]
    output = run.input_interface(namelist, "rrobin", 2)
    assert len(output) == 2
