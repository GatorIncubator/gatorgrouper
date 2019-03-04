# Contributing to GatorGrouper

First and foremost: thank you for taking the time to contribute to GatorGrouper!
The following is a quick guide to contributing to GatorGrouper, while
maintaining the integrity of the software.

## Table of Contents

* [Conduct](#conduct)
* [Contributing bug fixes](#contributing-bug-fixes)
* [Contributing features](#contributing-features)
* [Coding standards](#coding-standards)
  * [Code style](#code-style)
  * [Testing](#testing)
  * [Minimizing complexity](#minimizing-complexity)
* [Additional Notes](#additional-notes)

## Conduct

This project and the developers who work on it have agreed to adhere to this
[Conduct Guide](https://github.com/Allegheny-Computer-Science-203-S2019/cs203-S2019-conduct/blob/master/conduct.md).
By participating in the development of GatorGrouper, you will be expected to
adhere to this guide to the best of your ability.

## Contributing bug fixes

If you have found a bug:
 * First, check the [Issue Tracker](https://github.com/GatorEducator/gatorgrouper/issues)
   to see if the bug has already been found!
 * Once you are sure there is no existing Issue, you can
   [open a new issue](https://github.com/GatorEducator/gatorgrouper/issues/new).
   Write a **clear, descriptive title**, any information relevant to the bug
   (replicating the bug, specific usage problems, etc.), and provide a **code
   sample** or **executable test case** that demonstrates the anomalous
   behavior.

If you have written a patch for a bug:
  * Check the Issue Tracker for any relevant issues related to the bug.
  * If there are no relevant issues, [raise one](https://github.com/GatorEducator/gatorgrouper/issues/new).
    Indicate that you have written a patch for this bug.
  * Once you have found an issue or raised one, you can then [open a new pull
    request](https://github.com/GatorEducator/gatorgrouper/compare). Write a
    **clear description** of the bug and how you have patched it. Reference any
    relevant issues, or the new issue you have raised for the fix.
  * Check the [coding standards](#coding-standards) section to ensure that you
    have followed the coding conventions of GatorGrouper.

## Contributing features

If you have implemented a new feature for GatorGrouper:
  * Check the Issue Tracker for any issues relevant to your implemented feature.
  * [Open a new pull request](https://github.com/GatorEducator/gatorgrouper/compare).
    Write a **clear description** of the feature and its usage. In your pull
    request, be sure to have updated any relevant documentation to reflect the
    usage of the tool with your implemented features.
  * Be sure that you have followed the [coding standards](#coding-standards)
    outlined below for any code contributions you have made.

## Coding standards

By contributing source code to the GatorGrouper project, you are agreeing that
any code you have written follows the coding standards outlined below. This
means adhering to the style, testing, and complexity standards as follows.

### Code style

All GatorGrouper code should be written in Python. Code written for GatorGrouper
should,
  * Be written in a modular fashion, making use of functions and modules.
  * Be clearly documented with both docstring comments describing functions, as
    well as single line comments describing particularly complex lines of code.
  * Pass `flake8` checks without errors. You can learn more about using `flake8`
    [here](http://flake8.pycqa.org/en/latest/).
  * Score 10.0/10.0 when using the `pylint` tool. You can learn more about using
    `pylint` [here](https://www.pylint.org/).
  * Use the Python code formatter,
    [black](https://github.com/ambv/black). This will help with meeting the
    above requirements for both `flake8` and `pylint`. Furthermore, code not
    in the `black` format will fail the TravisCI build.

### Testing

Test cases for any implemented code **must** be provided. GatorGrouper uses the
`pytest` automated testing suite. `pytest` test cases should,
  * Cover the entirety of the code that is being executed. This means that there
    should be test cases for each and every function or method inside the
    program.
  * Be able to handle mutation testing to ensure that the test cases are
    accurate.
  * Have clear docstrings and doctests that allow developers to know what is
    being tested.

### Minimizing complexity

The definition of complexity we use is taken from “A Philosophy of Software
Design” by Chairman of Electric Cloud and Professor of Computer Science at
Stanford, John Ousterhout. John defines complexity as anything “related to the
structure of a software system that makes it hard to understand and modify the
system.” To this end, the standards here aim to minimize complexity by
maximizing the clarity and ease of modification of GatorGrouper. All
contributions to GatorGrouper should have the following qualities:

1. Changeability -
*Software shall be easily changeable to allow for future scalability.*
2. Uniqueness -
*Software shall not contain redundant features or code snippets.*
3. Encapsulation -
*Software shall be structured such that related documents are grouped together.*
4. Constraints -
*Software constraints should be clear to avoid confusing or arbitrary use-cases.*
5. Predictability -
*All software runs should have predictable and consistent outcomes.*
6. Feedback/Output -
*All software should have output that clearly displays the function attempted.*
7.  Documentation -
*All software should be properly documented and commented as to clearly convey
the purpose of the code.*

These standards are created and followed in order to effectively implement
GatorGrouper while minimizing the complexity of the code base.

## Additional Notes

GatorGrouper is a product of student work at Allegheny College. GatorGrouper is
developed under the [GatorEducator](https://github.com/GatorEducator/)
organization on GitHub. Contributors of GatorGrouper thank you for your
participation. Any questions about contributing not explained in this guide can
be answered by any contributor, raised in an issue on the Issue Tracker.

You can
[click here](#contributing-to-gatorgrouper) to return to the top of the page.
