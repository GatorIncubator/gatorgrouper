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

- `pip install --upgrade pip`
- `pip install -r requirements.txt`
- `pip install pytest-flake8`

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

## Running GatorGrouper

GatorGrouper accepts command line arguments and then generates output in your
terminal window. Using the defaults of storing your student identifiers in the
file called `students.txt` and creating groups of two students means that you
will run GatorGrouper with this command:

```
python3 gatorgrouper.py
```

Each of the previous commands were run on an Ubuntu 16.04 workstation running
Python 3.5.2. However, GatorGrouper should run correctly on a wide variety of
operating systems that support Python version 3.

## Problems or Praise

If you have any problems with installing or using GatorGrouper, then please
create an issue associated with this Git repository using the "Issues" link at
the top of this site. The contributors to GatorGrouper will do all that they can
to resolve your issue and ensure that the entire tool works well in your
teaching and development environment.
