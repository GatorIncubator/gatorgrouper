import group_random
import group_rrobin
import gatorgrouper


def test_group_random1():
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
    group_size = 3
    group_size2 = 2
    actual_output = group_random.group_random_group_size(list, group_size)
    actual_output2 = group_random.group_random_group_size(list2, group_size2)
    assert len(actual_output) == 4
    assert len(actual_output[0]) == 3
    assert len(actual_output2) == 3
    assert len(actual_output2[0]) == 2


def test_group_random_extra():
    """Testing the random type of grouping with a group of extra people not assigned to their own group"""
    responses = [
        [
            'Nick', True, False, True, False], [
            'Marvin', False, False, True, True], [
                'Evin', True, True, True, False], [
                    'Nikki', True, True, False, False], [
                        'Dan', False, True, False, True]]
    grpsize = 2
    returned_groups = group_random.group_random_group_size(responses, grpsize)
    assert len(returned_groups) == 2
    assert grpsize == 2


def test_group_random():
    """Testing the random type of grouping with everyone in an assigned group"""
    responses = [
        [
            'Nick', True, False, True, False], [
            'Marvin', False, False, True, True], [
                'Evin', True, True, True, False], [
                    'Nikki', True, True, False, False], [
                        'Dan', False, True, False, True], [
                            'Michael', True, True, False, False]]
    grpsize = 2
    returned_groups = group_random.group_random_group_size(responses, grpsize)
    assert len(returned_groups) == 3


def test_shuffle():
    """Checking the shuffle_students method for appropriate ouput"""
    student_identifiers = [
        "Dan",
        "Nikki",
        "Nick",
        "Jeff",
        "Austin",
        "Simon",
        "Jesse",
        "Maria"]
    shuffled_students = gatorgrouper.shuffle_students(student_identifiers)
    for i in range(0, len(shuffled_students)):
        assert (student_identifiers[i] in shuffled_students) is True
    assert (student_identifiers == shuffled_students) is False


def test_round_robin():
    """Testing the round robin function to assure proper output"""
    list = [
        ["Dan", True, True, True],
        ["Jesse", True, True, True],
        ["Austin", True, True, True],
        ["Nick", False, False, False],
        ["Nikki", False, False, False],
        ["Maria", False, False, False],
        ["Jeff", False, False, False],
        ["Simon", False, False, False],
        ["Jon", False, False, False],
        ["Angie", False, False, False],
        ["Izaak", False, False, False],
        ["Jacob", False, False, False]
    ]
    group_size = 3
    actual_output = group_rrobin.group_rrobin_group_size(list, group_size)
    assert len(actual_output) == 4
    assert len(actual_output[0]) == group_size
    assert (["Dan", True, True, True] in actual_output[0]) is True
    assert (["Jesse", True, True, True] in actual_output[2]) is True
    assert (["Austin", True, True, True] in actual_output[1]) is True

def test_rrobin_responses():
    list = [
        ["Dan", True, True, True],
        ["Jesse", True, True, True],
        ["Austin", True, True, True],
        ["Nick", False, False, False],
        ["Nikki", False, False, False],
        ["Maria", False, False, False],
        ["Jeff", False, False, False],
        ["Simon", False, False, False],
        ["Jon", False, False, False],
        ["Angie", False, False, False],
        ["Izaak", False, False, False],
        ["Jacob", False, False, False]
    ]
    group_size = 3
    list_output = group_rrobin.group_rrobin_num_group(responses, numgrps)
    assert list_output != 0
    #1. assert columns are not empty
    #2. assert responses are empty(groups are formed based on responses)
    #3. assert there is an average and a regular score


def test_random():
    """Testing the random grouping function to assure proper output"""
    list = [
        ["Dan", True, True, True],
        ["Jesse", True, True, True],
        ["Austin", True, True, True],
        ["Nick", False, False, False],
        ["Nikki", False, False, False],
        ["Maria", False, False, False],
        ["Jeff", False, False, False],
        ["Simon", False, False, False],
        ["Jon", False, False, False],
        ["Angie", False, False, False],
        ["Izaak", False, False, False],
        ["Jacob", False, False, False]
    ]
    group_size = 4
    actual_output = group_random.group_random_group_size(list, group_size)
    assert len(actual_output) == 3
    assert len(actual_output[0]) == 4
