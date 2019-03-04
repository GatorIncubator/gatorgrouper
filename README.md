# GatorGrouper

![logo](.github/gatorgrouper_logo.svg "GatorGrouper")

[![Build Status](https://api.travis-ci.org/GatorEducator/gatorgrouper.svg?branch=master)](https://travis-ci.org/GatorEducator/gatorgrouper)
[![codecov.io](http://codecov.io/github/GatorEducator/gatorgrouper/coverage.svg?branch=master)](http://codecov.io/github/GatorEducator/gatorgrouper?branch=master)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

Designed for use with [GitHub](https://github.com/), [GitHub Classroom](https://classroom.github.com/),
and [Travis CI](https://travis-ci.com/), GatorGrouper is an online group creation
tool to help facilitate group assignment in an educational setting.
While other group management tools create random groups, GatorGrouper
supports random and round robin style grouping with the option to specify
absentees. With creative implementation through a web application,
users can return to the site and update or re-group using previously
entered data.

GatorGrouper was created mainly in [Python 3](https://www.python.org/) and
utilizes the [Django](https://www.djangoproject.com/) web framework. Upon access
to the site, users are able to input student names and assign them to groups of
a specified size and method. The output of this program can be communicated to
the students in the class. If a course instructor is using [GitHub Classroom](https://classroom.github.com/),
they can invite the students in the class to create and join their assigned group.

## Installation

As a Python 3 program, GatorGrouper relies on
[pip](https://pip.pypa.io/en/stable/installing/) for installation. To ensure
that all of the dependencies are installed correctly, please type
the following commands before running GatorGrouper.

```shell
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

Note that you may have Python 3 setup in different ways on your computer. For
instance, you may prefer to install GatorGrouper's dependencies in a site-wide
location and then you would have to type `sudo pip install -r
requirements.txt`. Alternatively, you may choose to install the dependencies by
typing `pip install --user -r requirements.txt`.

GatorGrouper was developed to easily run in conjunction with a [venv-based
Python 3 virtual environment](https://docs.python.org/3/library/venv.html). This
means that if you are in the directory that contains `gatorgrouper`
then you could type `python3 -m venv gatorgrouper` to create all of
the components of a venv-based virtual environment in the `gatorgrouper`
directory. Once you complete this step, you can type the command `source
gatorgrouper/bin/activate` to activate the venv-based virtual environment.
Interested in learning more about the basics of virtual environments in Python
3? You can read this
[article](http://www.cs.allegheny.edu/sites/gkapfham/programming/research/idea/2017/07/14/Virtual-Environments/)
to further develop your understanding of this topic.

GatorGrouper requires users to use Python 3. You can type `python --version`
into the terminal window to check the current version of Python on your
workstation. If you do not have the right Python version, you can go to
[Python](https://www.python.org/downloads/) to download the latest version of
Python. If you can not download or upgrade Python on your workstation, you can
download the [Pyenv](https://github.com/pyenv/pyenv) tool to set up a virtual
environment for the newest Python version.

To install Pyenv, you can use [Pyenv Installer](https://github.com/pyenv/pyenv-installer)
by typing the command in terminal:

```shell
curl https://pyenv.run | bash
```

After the completion of this command, Pyenv should be installed. Please make
sure that you have the following lines in your `~/.bashrc` or similar file
types. Notices that different development evironment may have different
configuration configuration files (i.e., "dotfiles"). You can see more examples
and learn more in the instructions of Professor Kapfhammer's
[dotfiles](https://github.com/gkapfham/dotfiles) repository.

```shell
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Once Pyenv is installed, you can install the latest version of Python
for your Pyenv. We suggest developers to use `Python 3.7.2`  for `gatorgrouper`.
However, any version after `Python 3.6.8` would work well. To install, you
should restart your terminal window by typing `pyenv install 3.7.2`
and `pyenv global 3.7.2`.

After you finish this process, you should be able
to type `python --version` and get `Python 3.7.2` or other version after
`Python 3.6.8` in your terminal.

## Initial Setup

Ensure that you have installed gspread and oauth2client in the root
directory of the repository. In the terminal use the command:

```shell
python3 -m pip install --user gspread oauth2client
```

Create a Google Sheets spreadsheet and a Google Form in Google Drive. In the
Form, create yes or no questions to measure the capabilities and skills of the
students that you wish to group.  After you have at least one submission of the
Form, you can go to the responses tab and click on the green icon with the white
cross through it.  This will enable you to link the Sheet to the Form. You can
either create a new Sheet or link to a preexisting one. If you need to change
the destination, you can click on the three dot icon menu to the right of the
green icon and select "Select response destination".

Open the `.json` file in the `gatorgrouper` repository and find the `"client-email"`.
Copy the quoted text that looks like an email address. Return to the Sheet and
open the sharing options.  Paste the address and click send. Alternatively, if
you would like to create your own service account for confidentiality and
security, follow the tutorial found at [www.twolio.com](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)
to create a personal service account.

Within `defaults.py`, update the `DEFAULT_WORKBOOK` constant to the name of your
Sheet.

---

## Usage

GatorGrouper accepts command line arguments and then generates output in your
terminal window. Using the defaults of storing your student identifiers in the
file called `students.csv` and creating groups of two students means that you
will run GatorGrouper with this command:

```shell
python3 gatorgrouper.py
```

In order to see all the possible commands and their descriptions, enter
the following command:

```shell
python3 gatorgrouper.py -h
```

### Group Size

To specify the size of the groups, use the flag `--group-size`.

```shell
python3 gatorgrouper.py --group-size 4
```

This indicates that groups should each contain 4 members.  The provided group
size should be greater than 1 and equal to or less than half the total number of
students.  If the group size is not specified, the default group size is 3.

### Number of groups

To specify the number of groups the students should be placed in, use the flag
`--num-groups`.

```shell
python3 gatorgrouper.py --num-groups 4
```

This indicates that the students should be divided into 4 groups. The number of
groups should be at minimum 1 and at maximum the number of students to be placed
into groups. If the number of groups is not specified or is specified as '0' the
flag is ignored. This flag can be used along side `--absentees`, `--random`, and
`--round-robin`.

### Random Grouping Method

To randomly group the students, use the flag `--random`.

```shell
python3 gatorgrouper.py --random
```

This will randomly group the list of students you have provided, and is the
default grouping method used when none is provided. This method of grouping is
appropriate for cases where the assignment does not require that groups have a
minimum number of members that have responded as having a skill related to the
assignment. Consider using this method for assignments like in class exercises,
small discussion groups, or peer editing.

### Round-robin Grouping Method

To group students using the round-robin method, use the flag `--round-robin`.

```shell
python3 gatorgrouper.py --round-robin
```

The round-robin method takes the responses from the Sheet into account when
sorting students into groups.  The yes and no responses from the Sheet are
represented as true and false.  Round-robin randomizes the categories and
assigns a student, one at a time, to each group by using the first value
indicated as true.  When all of the students with true values are assigned,
it goes back and adds a student to each group until there are no students
remaining. This method of grouping is appropriate for cases where
the assignment or task would be more effective if every group had a relatively
even spread of students that responded as having a skill related to the
assignment. Consider using this method for assignments where students might have
specialized roles. Take for example a poll that asks the students if they would
be interested in taking on more responsibility as a team leader. Using the
random method and the -v flag to see additional output, GatorGrouper may produce
an output like this:

```
scores: [4, 4, 2, 0, 6, 4]
average: 3
```

The score of a group is determined by the amount of students that
answered "yes" to a particular question. In this example, there is
one group that has no students that are willing to be a team leader.
However if you use the round robin grouping method, one possible
output would be:

```
scores: [4, 6, 4, 2, 2, 2]
average: 3
```

In this case, the average score is the same as with the random grouping method,
but all the groups have atleast one student willing to be a team leader. This
has the potential to make the assignment more effective by maximizing team
effectiveness.

### Absent Students

To indicate which students are absent so they are not grouped, use the
flag `--absentees`.  The arguments can be entered in the following ways:

```shell

python3 gatorgrouper.py --absentees student1 student2
python3 gatorgrouper.py --absentees 'student1' 'student2'
python3 gatorgrouper.py --absentees "student1" "student2"
```

Note that the absent students' names must be separated by spaces, not quotes.
The names can be surrounded by single or double quotes if desired.

If no absentees are indicated with this flag, then the program will assume that
there are no students absent.

### Specify File Containing List of Students

To bypass the Google Forms integration and instead supply a list of students
directly to the program, use the `--students-file` flag.

```shell
python3 gatorgrouper.py --students-file "file_name.csv"
python3 gatorgrouper.py --students-file file_name.csv
```

### Monitoring GatorGrouper

To see detailed general output to monitor progress, use the flag `-v` or
`--verbose`.

```shell
python3 gatorgrouper.py --verbose
```

To see detailed technical output to diagnose problems, use the flag `-d` or
`--debug`.

```shell
python3 gatorgrouper.py --debug
```

If neither of these flags are set, logging will only be shown if an error occurs.

### Full Example

```shell
$ python3 gatorgrouper.py --group-size 3 --absentees becky george --random

GatorGrouper: Automatically Assign Students to Groups
https://github.com/GatorEducator/gatorgrouper

Successfully placed 9 students into 3 groups

Group 1
smithj
robertss
johnsont

Group 2
peggys
stevensons
ronp

Group 3
georgeh
youngr
harrisonf
```

Each of the previous commands were run on an Ubuntu 16.04 workstation running
Python 3.5.2. However, GatorGrouper should run correctly on a wide variety of
operating systems that support Python version 3.

---

## Testing

### Functions Tested

The test suite is designed to test the different functions of `gatorgrouper.py`.
The first function the test suites test is to make sure that there are the
correct amount of students in each group. The test suite also makes sure that
the shuffle function is working correctly. There are also test cases to make
sure that the professor has the option to mark students absent, and these
students will not get grouped. Lastly, the test suite test checks to see if
students are being correctly grouped based on category.

### Running the Test Suite

The test suite requires `pytest-flake8`, which can be installed with the
following command:

```shell
pip3 install --user pytest-flake8
```

From the root directory, the test suite can be ran with the following command:

```shell
python3 -m pytest tests
```

### Automatic Linting

For any future issues with linting, you can install an autolinting tool with:

```shell
pip3 install --user autopep8
```

To run the tool, type the following into the main directory.

```shell
autopep8 --in-place --aggressive *.py
```

If there are any linting issues that were not fixed by the tool, the error
message from the test suite will direct you to where the issue is and tell you
what it is in order for you to fix it.

## Test Coverage

Test coverage reporting is handled with `pytest-coverage`.  The following
commands will install and run `pytest-coverage`.

```shell
pip install pytest-cov
coverage run --source tests -m py.test
coverage report
```

## Problems or Praise

If you have any problems with installing or using GatorGrouper, then please
create an issue associated with this Git repository using the "Issues" link at
the top of this site. The contributors to GatorGrouper will do all that they can
to resolve your issue and ensure that the entire tool works well in your
teaching and development environment.
