import pytest
import parse_arguments
import hypothesis
import group_random
import group_rrobin
import gatorgrouper


from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers
from hypothesis.strategies import text


@given(group_size=integers(min_value=1, max_value = 3))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_group_random1(group_size):
    """Testing that the group_random() function creates the
        appropriate number of groups with the appropriate number"""
    list = [
        "Austin",
        "Dan",
        "Angie",
        "Cullen",
        "Chase",
        "Vinny",
        "Nick",
        "Jeff",
        "James",
        "Kelly",
        "Nikki",
        "Robert"]
    list2 = ["Dan", "Angie", "Austin", "Izaak", "Nick", "Jeff"]
    size_count = group_size
    actual_output = group_random.group_random_group_size(list, group_size)
    actual_output2 = group_random.group_random_group_size(list2, group_size)

    assert len(actual_output) == 12/size_count
    assert len(actual_output[0]) == size_count
    assert len(actual_output2) == 6/size_count
    assert len(actual_output2[0]) == size_count
