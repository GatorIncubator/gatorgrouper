""" GatorGrouper randomly assigns a list of students to groups """

import sys
import logging

from gatorgrouper.utils import parse_arguments
from gatorgrouper.utils import read_student_file
from gatorgrouper.utils import display
from gatorgrouper.utils import constants
from gatorgrouper.utils import group_genetic
from gatorgrouper.utils import mutations
from gatorgrouper.utils import run


if __name__ == "__main__":  # pragma: no cover

    # parse the arguments and display welcome message
    GG_ARGUMENTS = parse_arguments.parse_arguments(sys.argv[1:])
    display.display_welcome_message()
    logging.info("Configuration of GatorGrouper:")
    logging.debug(GG_ARGUMENTS)

    # read in the student identifiers from the specified file
    input_list = read_student_file.read_csv_data(GG_ARGUMENTS.file)
    if GG_ARGUMENTS.preferences is None:
        preference = None
    else:
        preference = dict(read_student_file.read_csv_data(GG_ARGUMENTS.preferences))
    check_if_arguments_valid = parse_arguments.check_valid(GG_ARGUMENTS, input_list)
    if check_if_arguments_valid is False:
        print("Incorrect command-line arguments.")
        sys.exit(1)
    else:
        GROUPED_STUDENT_IDENTIFIERS = run.run_arguments(GG_ARGUMENTS, preference)

        # report generated groups
        display.display_student_groups(GROUPED_STUDENT_IDENTIFIERS)
