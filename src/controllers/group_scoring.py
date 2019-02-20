""" score groups by approximate level of diversity """


def score_group(student_identifers):
    """ score single group """
    score = 0
    for student in student_identifers:
        for category in range(len(student[1:])):
            if student[category + 1] is True:
                score += 1
    return score


def score_groups(student_groups):
    """ score multiple groups """
    scores = []
    ave = 0
    for group in student_groups:
        scores.append(score_group(group))
        ave += score_group(group)
    ave = int(ave / len(student_groups))
    # returns the scores of each group as well as the average score
    return scores, ave
