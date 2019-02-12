from flake8.api import legacy as flake8
import glob
import os


# Linting Tests
# def test_flake8():
#
#     # list of all file names to be checked for PEP8
#     filenames = list()
#
#     # fill list with all python files found in all subdirectories
#     for root, dirs, files in os.walk("gatorgrouper", topdown=False):
#         pyFiles = glob.glob(root + "/*.py")
#         filenames.extend(pyFiles)
#
#     style_guide = flake8.get_style_guide(ignore=["E265", "E501"])
#     report = style_guide.check_files(filenames)
#     assert report.get_statistics('E') == [], 'Flake8 found violations'
