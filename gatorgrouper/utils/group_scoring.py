""" score groups by approximate level of diversity """


from typing import List, Tuple, Union


# pylint: disable=bad-continuation
def score_group(
    student_identifers: Union[List[List[Union[str, bool]]], List[str]]
) -> int:
    """ score single group """
    score = 0
    for student in student_identifers:
        for category in range(len(student[1:])):
            if student[category + 1] is True:
                score += 1
    return score


def calculate_avg(
    student_groups: Union[List[List[str]], List[List[List[Union[str, bool]]]]]
) -> Tuple[List[int], int]:
    """ Utilizes score_group in order to find the mean for all of the groups """
    scores = []
    ave = 0
    for group in student_groups:
        scores.append(score_group(group))
        ave += score_group(group)
    ave = int(ave / len(student_groups))
    # returns the scores of each group as well as the average score
    return scores, ave


# def score_group_conflicts(student_indentifiers):
#    """ conflict score single group """
#    conflict_score = 0
#    for student in student_identifiers:
#       for conflict
#    return conflict_score


def score_group_conflicts(student_groups):
    """ score group conflicts """
    conflict_scores = []
    conflict_ave = 0
    for group in student_groups:
        conflict_scores.append(score_group_conflict(group))
        conflict_ave += score_group_conflict(group)
    conflict_ave = int(ave / len(student_groups))


return conflict_scores, conflict_ave
