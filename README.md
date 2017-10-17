# GatorGrouper

GatorGrouper is a Python 3 program that assigns a list of students to groups of
a specified size. The output of this program could then be communicated to the
students in a specific class. Then, if a course instructor is using [GitHub
Classroom](https://classroom.github.com/), you can ask the students in your
class to create and join their assigned group.

## Installing GatorGrouper

As a Python 3 program, GatorGrouper relies on
[pip](https://pip.pypa.io/en/stable/installing/) for installation. To ensure
that all of the dependencies are installed correctly, please type
the following commands before running GatorGrouper.

```
pip install --upgrade pip
pip install -r requirements.txt
```

Note that you may have Python 3 setup in different ways on your computer. For
instance, you may prefer to install GatorGrouper's dependencies in a site-wide
location and then you would have to type, for instance, `sudo pip install -r
requirements.txt`. Alternatively, you may choose to install the dependencies by
typing `pip install --user -r requirements.txt`.

GatorGrouper was developed to easily run in conjunction with a [venv-based
Python 3 virtual environment](https://docs.python.org/3/library/venv.html). This
means that if you are in the directory that contains the `gatorgrouper`
directory then you could type `python3 -m venv gatorgrouper` to create all of
the components of a venv-based virtual environment in the `gatorgrouper`
directory. Once you complete this step, you can type the command `source
gatorgrouper/bin/activate` to activate the venv-based virtual environment.
Interested in learning more about the basics of virtual environments in Python
3? You can read this
[article](http://www.cs.allegheny.edu/sites/gkapfham/programming/research/idea/2017/07/14/Virtual-Environments/)
to further develop your understanding of this topic.

## Initial Setup of GatorGrouper

Ensure that you have installed gspread and oauth2client installed in the root
directory of the repository.  In the terminal use the command:

```
python3 -m pip install --user gspread oauth2client
```

Create a Google Sheets spreadsheet and a Google Form in Google Drive.  In the
Form, create yes or no questions to measure the capabilities and skills of the
students that you wish to group.  After you have at least one submission of the
Form, you can go to the responses tab and click on the green icon with the white
cross through it.  This will enable you to link the Sheet to the Form.  You can
either create a new Sheet or link to a preexisting one.  If you need to change
the destination, you can click on the three dot icon menu to the right of the
green icon and select "Select response destination".

Open the `.json` file in the `gatorgrouper` repository and find the `"client-email"`.
Copy the quoted text that looks like an email address.  Return to the Sheet and
open the sharing options.  Paste the address and click send.  Alternatively, if
you would like to create your own service account for confidentiality and
security, follow the tutorial found at [www.twolio.com](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)
to create a personal service account.

Within `spreadsheet.py`, find `sheet = client.open("Compsci280 Lab4 Survey
Results").sheet1` and change `"Compsci280 Lab4 Survey Results"` to the name of
your Sheet.

## Running GatorGrouper

GatorGrouper accepts command line arguments and then generates output in your
terminal window. Using the defaults of storing your student identifiers in the
file called `students.txt` and creating groups of two students means that you
will run GatorGrouper with this command:

```
python3 gatorgrouper.py
```

### Group Size

To specify the size of the groups, use the flag `---groupsize`.

Example:

```
python3 gatorgrouper.py --group-size 3
```

This indicates that groups should each contain 3 members.

The group size should be greater than 1 and equal to or less than
half the total number of students. If the group size is not
specified, the default group size is 2.

### Grouping Methods

#### Random Method

To randomly group the students, use the flag `--random`.

Example:

```
python3 gatorgrouper.py --random
```

This will randomly group the list of students you have provided.

#### Round-robin Method

To group students using the round-robin method, use the flag `--round-robin`.

Example:

```
python3 gatorgrouper.py --round-robin
```

The round-robin method takes the responses from the Sheet into account when
sorting students into groups.  The yes and no responses from the Sheet are
represented as true and false.  Round-robin randomizes the categories and
assigns a student, one at a time, to each group by using the first value
indicated as true.  When all of the students with true values are assigned,
it goes back and adds a student to each group until there are no students
remaining.

If none of these flags are used, the groups will be generated randomly.

### Absentees

To indicate which students are absent so they are not grouped, use the
flag `--absentees`.

Example:

The arguments can be entered in the following ways:

```
python3 gatorgrouper.py --absentees student1, student2
python3 gatorgrouper.py --absentees 'student1', 'student2'
python3 gatorgrouper.py --absentees "student1", "student2"
python3 gatorgrouper.py --absentees student1 student2
python3 gatorgrouper.py --absentees 'student1' 'student2'
python3 gatorgrouper.py --absentees "student1" "student2"
```

If no absentees are indicated with this flag, then the program will assume that
there are no students absent.

### Specify File Containing List of Students

To specify a different file other than the default `students.txt`, use the
flag `--students-file`.

Example:

```
python3 gatorgrouper.py --students-file "students_list.txt"
python3 gatorgrouper.py --students-file students_list.txt
```

### Monitoring GatorGrouper

To see detailed general output to monitor progress, use the flag `-v` or
`--verbose`.

Example:

```
python3 gatorgrouper.py --verbose
```

To see detailed technical output to diagnose problems, use the flag `-d` or
`--debug`.

Example:

```
python3 gatorgrouper.py --debug
```

If none of these flags are used, logging will only be shown if an error occurs.

### Sample Use of GatorGrouper

```
$ python3 gatorgrouper.py --group-size 3 --absentees becky, george --random

GatorGrouper: Automatically Assign Students to Groups
https://github.com/gkapfham/gatorgrouper

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

## Testing Documentation

### Functions

The test suite is designed to test the different functions of gatorgrouper.py.
The first function the test suites test is to make sure that there are the
correct amount of students in each group. The test suite also makes sure that
the shuffle function is working correctly. There are also test cases to make
sure that the professor has the option to mark students absent, and these
students will not get grouped. Lastly, the test suite test checks to see if
students are being correctly grouped based on category.

### Run

Test suites for the gatorgrouper.py module

run with `pytest test_gatorgrouper.py from the gatorgrouper/tests directory`
Requires `pip3 install pytest-flake8` in order to run.

`pip3 install pytest-flake8`

Linting:

For any future issues with linting, you can install an autolinting tool with:

`pip3 install autopep8`

To run the tool, type the following into the main directory.

`autopep8 --in-place --aggressive --aggressive *.py`

If there are any linting issues that were not fixed by the tool, the error
message from the test suite will direct you to where the issue is and tell you
what it is in order for you to fix it.

## Tox Testing Tool

The tox testing tool was not sucessfully implemented due to time contraints, so
GatorGrouper is only confirmed to run in Python 3.5.

## Installation of Pytest-Coverage
run in the terminal:<br/>
```
pip install pytest-cov
```
## Usage
to run pytest-coverage:<br/>
```
coverage run --source tests -m py.test
coverage report
```
## Configuring Travis-Ci
In order to activate travis-ci you must have admin rights.<br/>
Make sure that you turned on the repo by seeing the green slide.<br/>
Then in the root directory of your repo create a .travis.yml<br/>
An example of a .travis.yml
```
language: python
python:
  - "3.5"

cache:
  directories:
    - $HOME/.pip-cache/
# install mdl for checking Markdown
before_install:
  - gem install mdl
notifications:
  email: never

install:
  - pip install --upgrade pip
  - python3 -m pip install -r requirements.txt
  - pip3 install pytest-flake8
  - pip3 install pytest-cov
  - pip3 install autopep8
  - pip3 install gspread oauth2client
  - pip3 install coveralls
  
script:
  - pytest tests
  - mdl README.md
  - coverage run --source tests -m py.test 
  - coverage report 
```

##Activating Coveralls
Go to https://coveralls.io/sign-up<br/>
Click Github Sign Up<br/>
Add Repo GKAPFHAM/ gatorgrouper(make sure it is on)<br/>
You should now see it in your repos click on Gator Grouper.<br/>
The now add to the end of your .travis.yml:<br/>
```
after_success:
  coveralls
```
## Problems or Praise

If you have any problems with installing or using GatorGrouper, then please
create an issue associated with this Git repository using the "Issues" link at
the top of this site. The contributors to GatorGrouper will do all that they can
to resolve your issue and ensure that the entire tool works well in your
teaching and development environment.

[![Coverage Status](https://coveralls.io/repos/github/GatorGrouper/gatorgrouper/badge.svg?branch=master)](https://coveralls.io/github/GatorGrouper/gatorgrouper?branch=master)
