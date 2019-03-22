# GatorGrouper

![logo](.github/gatorgrouper_logo.png "GatorGrouper")

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

As a Python 3 program, GatorGrouper relies on
[Pipenv](https://github.com/pypa/pipenv) for the installation of the libraries that
it depends on and the creation of the virtual environments in which it
runs. To install GatorGrouper, you should first follow Pipenv's installation
instructions. You should also ensure that you have installed Git on your
computer and that you can run Git commands in a terminal window. Then, you can
type the following command in your terminal window to clone GatorGrouper's GitHub
repository:

```
git clone git@github.com:GatorEducator/gatorgrouper.git
```

If you plan to develop new features for GatorGrouper or if you want to run the
tool's test suite in [Pytest](https://github.com/pytest-dev/pytest), then you should
install the developer dependencies by running `pipenv install --dev`
in the directory that was cloned. If you only want to use GatorGrouper,
then you can type `pipenv install` instead. Once these commands complete
successfully, that's all you have to do to install GatorGrouper!

## Testing GatorGrouper

GatorGrouper uses [Pytest](https://docs.pytest.org/en/latest/) for testing.
Depending on your goals, there are several different configurations in which you
can run the provided test suite. If you want to run the test suite to see if all
of the test cases are correctly passing, then you can type the following
command in your terminal window:

```
pipenv run pytest
```

Please note that you must preface the execution of the test suite with the
command `pipenv run` if you want to ensure that the tests run with the correct
access to their Python packages and in the desired virtual environment. The
provided command runs `pytest` explicitly. If you are using GatorGrouper and you
find that a test fails in your development environment, please raise an issue in
GatorGrouper's issue tracker. With that said, if you are developing new features
for Pytest and you want it to produce console output and stop when it runs the
first failing test, you can type:

```
pipenv run pytest -x -s
```

---

## Usage

GatorGrouper accepts command line arguments and then generates output in your
terminal window. The program requires user to provide an input `.csv` file.
This will create groups of three students means that you will run GatorGrouper
with this command:

```shell
pipenv run python3 gatorgrouper_cli.py --file filepath
```

In order to see all the possible commands and their descriptions, enter
the following command:

```shell
pipenv run python3 gatorgrouper_cli.py -h
```

### Details with Importing Input File

Since input file is required, use the `--file` flag to let GatorGrouper know
the path of the file you are using. Please make sure the input file has more than
six students. Otherwise you should change both group size and number of groups
to a value larger than 1 and smaller than half of the total number of students.

```shell
pipenv run python3 gatorgrouper_cli.py --file filepath
```

### Number of groups

To specify the number of groups the students should be placed in, use the flag
`--num-groups`.

```shell
pipenv run python3 gatorgrouper_cli.py --file filepath --num-groups 4
```

This indicates that the students should be divided into 4 groups. The number of
groups should be at minimum 2 and at maximum the number of half of the students to
be placed into groups. This flag can be used along side `--absentees`, `--method=random`,
and `--method=rrobin`.

### Random Grouping Method

To randomly group the students, use the flag `--method=random`.

```shell
pipenv run python3 gatorgrouper_cli.py --file filepath --method=random
```

This will randomly group the list of students you have provided, and is the
default grouping method used when none is provided. Additionally, the random
grouping method allows for recognition of student conflicts via a numerical,
lower-is-better representation (e.g a level 1 conflict is for students who
don't like one another while a level 5 conflict is for students who are legally
mandated to be separated). The random method will take in that conflict, apply
it to both students and then group the students, attempting to minimize the
overall level of conflict within the group through iterating through the
function an arbitrary amount of times, creating groups with less and less
conflict.

### Round-robin Grouping Method

To group students using the round-robin method, use the flag `--method=rrobin`.

```shell
pipenv run python3 gatorgrouper_cli.py --file filepath --method=rrobin
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
but all the groups have at least one student willing to be a team leader. This
has the potential to make the assignment more effective by maximizing team
effectiveness.

### Absent Students

To indicate which students are absent so they are not grouped, use the
flag `--absentees`.  The arguments can be entered in the following ways:

```shell
pipenv run python3 gatorgrouper_cli.py --file filepath --absentees "student1" "student2"
```

Note that the absent students' names must be separated by spaces, not quotes.
The names can be surrounded by single or double quotes if desired.

If no absentees are indicated with this flag, then the program will assume that
there are no students absent.

### Monitoring GatorGrouper

To see detailed general output to monitor progress, use the flag `-v` or
`--verbose`.

```shell
pipenv run python3 gatorgrouper_cli.py --verbose
```

To see detailed technical output to diagnose problems, use the flag `-d` or
`--debug`.

```shell
pipenv run python3 gatorgrouper_cli.py --debug
```

If neither of these flags are set, logging will only be shown if an error occurs.

### Kernighan-Lin Grouping Method

The Kernighan-Lin algorithm creates a k-way graph partition that determines the
grouping of students based on their preferences for working with other students
and compatibility with other classmates. The graph recognizes student compatibility
through numerical weights (indicators of student positional relationship on the graph).
This grouping method allows for a systematic approach and balanced number of student
groups capable of tackling different types of work. Students should enter student
name, number of groups, objective weights (optional), objective_measures(optional),
students preferred to work with (optional), preference weight(optional),
and preferences_weight_match(optional). Note that number of groups must be at
least 2 and be a power of 2, i.e. 2, 4, 8...

NOTE: `--method graph` and `--num-group` are required to create groups.

It is required to use the graph argument to generate groups through the graph
partitioning. To generate groups using the Kernighan-Lin grouping algorithm use
the flag `--method graph`

```shell
pipenv run python gatorgrouper_cli.py --file filepath --method graph
--num-group NUMBER
```

To load student preferences, a preference weight, use the flag `--preferences`

```shell
pipenv run python gatorgrouper_cli.py --file filepath --method graph
--num-group NUMBER --preferences filepath
```

To indicate student preference weight use the flag `--preferences_weight`

```shell
pipenv run python gatorgrouper_cli.py --file filepath --method graph
--num-group NUMBER --preferences filepath --preferences_weight PREFERENCES_WEIGHT
```

To indicate preference weight match use the flag `--preferences_weight_match`

```shell
pipenv run python gatorgrouper_cli.py --file filepath --method graph
--num-group NUMBER --preferences filepath --preferences_weight PREFERENCES_WEIGHT
--preferences_weight_match PREFERENCES_WEIGHT_MATCH
```

To add objective measures use the flag `--objective_measures`

```shell
pipenv run python gatorgrouper_cli.py --file filepath --method graph
--num-group NUMBER --objective_measures LIST --objective_weights LIST
```

To add objective weights use the flag `--objective_weights`

```shell
pipenv run python gatorgrouper_cli.py --file filepath --method graph
--num-group NUMBER --objective_measures LIST --objective_weights LIST
```

A command line of all agruments would be:

```shell
pipenv run python gatorgrouper_cli.py --file filepath --method graph
--num-group NUMBER --preferences filepath --preferences-weight PREFERENCES_WEIGHT
--preferences-weight-match PREFERENCES_WEIGHT_MATCH --objective-measures LIST
--objective-weights LIST
```

### Full Example

```shell
$ pipenv run python3 gatorgrouper_cli.py --file /home/w/wuj/cs203S2019/lab/students.csv
--absentees becky george --method=random

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

## Django

Django is a free and open source web application framework that is written in
Python and helps to implement websites in a convenient manner. With the collection
of modules embedded within its framework, development is made easier and one
would not have to work on creating the website from scratch but just use the
components that are already built within which saves a lot of time. Acknowledging
the fact that we have a short span of time to work on the GatorGrouper project,
we decided to use Django as it provides the developer with simpler tools to grasp
the project's structure. In addition to this, it supports Object-Relational
Mapping, which allows the user to create a bridge between the data model and the
database engine, and supports a large set of database systems including SQLite.

### Running

In order to run the application, type in this command in the terminal:

```shell
pipenv run python manage.py runserver
```

To check if your server is set up and running, open up your browser and
type:

```shell
localhost:8000
```

### Testing Django Framework

In order to run the testing, type in this command in the terminal:

```shell
pipenv run pytest tests --cov-config pytest.cov --cov
```

### Design and Configuration

The web applications in Django have access to the data and manage it through
objects in Python which are referred to as models. A model is a special type of
object that is saved in the database. It defines the structure of the stored data,
includes the field types along with their size if possible, and contains behaviors
of the data that is being stored. After creating the model structure for the
project, Django handles all the communication that goes within it.

The Django web framework comes with a built-in object-relational mapping module,
ORM, which allows interaction with the database in an object-oriented setup. It
allows the users to have access to the stored data in the database. This technique
builds a bridge between the data tables, field, and the Python objects. ORM allows
the developer to work with Python code instead of SQL to work with the data schemas
in their database. This approach allows the developers to work with a database in
a programming language they prefer instead of a database management language.

Prior to dealing with ORM, we define model classes that translate to data tables
and the relation between them. For the GatorGrouper project, we created six classes
entitled as: Professor, Classes, Assignment, Students, Traits, and Grouped
Students. In order to establish a relationship between these classes, we define
foreign keys using `django.db.models.ForeignKey`. The different entities within
the classes are linked by a means one-to-many, many-to-one, and many-to-many
relationship.

### Set Up a Python Virtual Environment with Django

Step 1: Create a virtual environment named eb-virt.
On Unix-based systems, such as Linux or OS X, enter the following command:

```
~$ virtualenv ~/eb-virt
```

On Windows, enter the following command:

```
C:\> virtualenv %HOMEPATH%\eb-virt
```

Step 2: Activate the virtual environment.
On Unix-based systems, enter the following command:

```
~$ source ~/eb-virt/bin/activate
(eb-virt) ~$
```

On Windows, enter the following command:

```
C:\>%HOMEPATH%\eb-virt\Scripts\activate
(eb-virt) C:\>
```

You will see (eb-virt) prepended to your command prompt, indicating that you're
in a virtual environment.
Note:
The remainder of these instructions show the Linux command prompt in your home
directory ~$. On Windows this is C:\Users\USERNAME>, where USERNAME is your
Windows login name.

Step 3: Use pip to install Django.

```
(eb-virt)~$ pip install django==2.1.1
```

Note:
The Django version you install must be compatible with the Python version on
the Elastic Beanstalk Python configuration that you choose for deploying your
application. For deployment details, see Deploy Your Site With the EB CLI in
this topic. For details on current Python configurations, see Python in the
AWS Elastic Beanstalk Platforms document.
For Django version compatibility with Python, see What Python version can I
use with Django?

Step 4: To verify that Django has been installed, type:

```
(eb-virt)~$ pip freeze
Django==2.1.1
...
```

This command lists all of the packages installed in your virtual environment.
Later you will use the output of this command to configure your project for use
with Elastic Beanstalk.

### Configure Your Django Application for Elastic Beanstalk

Now that you have a Django-powered site on your local machine, you can configure
it for deployment with Elastic Beanstalk.
By default, Elastic Beanstalk looks for a file called application.py to start
your application. Since this doesn't exist in the Django project that you've
created, some adjustment of your application's environment is necessary. You
will also need to set environment variables so that your application's modules
can be loaded.

To configure your site for Elastic Beanstalk
Step 1: Activate your virtual environment.
On Linux-based systems, enter the following command:

```
~/ebdjango$ source ~/eb-virt/bin/activate
```

  On Windows, enter the following command:

```
C:\Users\USERNAME\ebdjango>%HOMEPATH%\eb-virt\Scripts\activate
```

Step 2: Run pip freeze and save the output to a file named requirements.txt:

```
(eb-virt) ~/ebdjango$ pip freeze > requirements.txt
```

Elastic Beanstalk uses requirements.txt to determine which package to install on
the EC2 instances that run your application.

Step 3: Create a new directory, called .ebextensions:

```
(eb-virt) ~/ebdjango$ mkdir .ebextensions
```

Step 4: Within the .ebextensions directory, add a configuration file named
django.config with the following text:

Example ~/ebdjango/.ebextensions/django.config

```
option_settings:
aws:elasticbeanstalk:container:python:
WSGIPath: ebdjango/wsgi.py
```

This setting, WSGIPath, specifies the location of the WSGI script that Elastic
Beanstalk uses to start your application.

Step 5: Deactivate your virtual environment by with the deactivate command:

```
(eb-virt) ~/ebdjango$ deactivate
```

Reactivate your virtual environment whenever you need to add additional packages
to your application or run your application locally.

### Deploy

To create an environment and deploy your Django application:

Step 1: Initialize your EB CLI repository with the eb init command:

```
~/ebdjango$ eb init -p python-3.6 django-tutorial
Application django-tutorial has been created.
```

This command creates a new application named django-tutorial and configures your
local repository to create environments with the latest Python 3.6 platform
version.

Step 2: (optional) Run eb init again to configure a default keypair so that you
can connect to the EC2 instance running your application with SSH:

```
~/ebdjango$ eb init
Do you want to set up SSH for your instances?
(y/n): y
Select a keypair.
1) my-keypair
2) [ Create new KeyPair ]
```

Step 3: Create an environment and deploy you application to it with eb create:

```
~/ebdjango$ eb create django-env
```

Step 4: When the environment creation process completes, find the domain name of
your new environment by running eb status:

```
~/ebdjango$ eb status
```

Step 5: Edit the settings.py file in the ebdjango directory, locate the
ALLOWED_HOSTS setting, and then add your application's domain name that you
found in the previous step to the setting's value. If you can't find this
setting in the file, add it to a new line.

```
...
ALLOWED_HOSTS = ['eb-django-app-dev.elasticbeanstalk.com']
```

Step 6: Save the file, and then deploy your application by running eb deploy.
When you run eb deploy, the EB CLI bundles up the contents of your project
directory and deploys it to your environment.

```
~/ebdjango$ eb deploy
```

Step 7: When the environment update process completes, open your web site with
eb open:

```
~/ebdjango$ eb open
```

This will open a browser window using the domain name created for your
application. You should see the same Django website that you created and
tested locally.

## Problems or Praise

If you have any problems with installing or using GatorGrouper, then please
create an issue associated with this Git repository using the "Issues" link at
the top of this site. The contributors to GatorGrouper will do all that they can
to resolve your issue and ensure that the entire tool works well in your
teaching and development environment.
