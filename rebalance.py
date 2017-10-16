""" rebalance groups by swapping lowest with highest scoring """

from group_scoring import score_groups


def rebalance(student_groups, scores, ave):
    """rebalances the groups of students"""

    # average score of the groups
    ave = int(ave / len(scores))
    #print("average score: "+str(ave))
    #print("Threshold: "+str(int(ave*(2/3))))

    if int(ave*(2/3))-1 in scores:
        #print("Students not well distributed")
        # stores the student with the highest value in the highest valued group
        temp = max(student_groups[scores.index(max(scores))])
        # stores the student with the lowest value in the lowest valued grouop
        lowest = min(student_groups[scores.index(min(scores))])
        # switches the highest and lowest valued students
        student_groups[scores.index(max(scores))].insert(scores.index(max(scores)), lowest)
        student_groups[scores.index(max(scores))].remove(temp)
        student_groups[scores.index(min(scores))].insert(scores.index(min(scores)), temp)
        student_groups[scores.index(min(scores))].remove(lowest)
        # reevaluates scores
        score_groups(student_groups)
