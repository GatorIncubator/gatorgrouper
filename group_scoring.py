""" score groups by approximate level of diversity """


def score_group(student_identifers):
    """ score single group """
    score = 0
    for student in student_identifers:
        for category in range(len(student[1:])):
            #print(student[category+1])
            if student[category+1] == True:
                score += 1
        #print()
    #print(score)
    return score


def score_groups(student_groups, group_size):
    """ score multiple groups """
    scores = []
    ave = 0
    for group in student_groups:
        scores.append(score_group(group))
        ave += score_group(group)
	#average score of the groups
    ave = int(ave / len(scores))
    #print("average score: "+str(ave))
    #print("Threshold: "+str(int(ave*(2/3))))
    if int(ave*(2/3))-1 in scores:
        #print("Students not well distributed")
		#stores the student with the highest value in the highest valued group
        temp = max(student_groups[scores.index(max(scores))])
		#stores the student with the lowest value in the lowest valued grouop
        lowest = min(student_groups[scores.index(min(scores))])
		#switches the highest and lowest valued students
        student_groups[scores.index(max(scores))].insert(scores.index(max(scores)), lowest)
        student_groups[scores.index(max(scores))].remove(temp)
        student_groups[scores.index(min(scores))].insert(scores.index(min(scores)), temp)
        student_groups[scores.index(min(scores))].remove(lowest)
		#reevaluates scores
        score_groups(student_groups, group_size)
