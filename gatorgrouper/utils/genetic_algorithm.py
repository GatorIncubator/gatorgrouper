"""Generate grouping based on student skills and preferences."""
from typing import List
import random
from colors import bold
import numpy as np
import workbook
import math


class Student:
    """Represent student."""
    def __init__(self, email: str, skills: List[int], preferences: List[str]):
        self.email = email
        self.skills = skills
        self.preferences = preferences

    def __str__(self):
        student_str = self.email + "\n"
        student_str += "\tPreferences: " + str(self.preferences) + "\n"
        student_str += "\tSkills: " + str(self.skills)
        return student_str

    def __repr__(self):
        return self.email

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.email == other.email
        return NotImplemented

    def __hash__(self):
        return hash(self.email)


class Individual:
    """Represent individual."""
    def __init__(self, grouping: List[List[Student]], fitness):
        self.grouping = grouping
        self.fitness = fitness

    def __str__(self):
        grouping_str = ""
        for number, group in enumerate(self.grouping):
            grouping_str += "Group {}".format(number) + "\n"
            for student in group:
                grouping_str += str(student) + "\n"
        return bold("Grouping\n") + grouping_str + bold("Fitness\n") + str(self.fitness)


class Fitness:
    """Represent fitness. Variables range from 0 to 1."""
    def __init__(self, preference, balance, fairness):
        self.preference = preference
        self.balance = balance
        self.fairness = fairness
        # FIXME: Can give weights to each variable
        self.value = 0.5 * preference + 3.0 * balance + 1.5 * fairness

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        string = "Preference: " + str(self.preference) + "\n"
        string += "Balance: " + str(self.balance) + "\n"
        string += "Fairness: " + str(self.fairness) + "\n"
        string += "Value: " + str(self.value) + "\n"
        return string


best_grouping = list()
best_fitness = Fitness(0, 0, 0)


def create():
    students_to_group = workbook.STUDENTS[:]
    random.shuffle(students_to_group)

    grouping = list()

    for _ in range(workbook.GROUPING_SIZE):
        grouping.append(list())

    for index, student in enumerate(students_to_group):
        grouping[index % workbook.GROUPING_SIZE].append(student)

    if len(grouping) < 1:
        print("CREATED TOO SMALL GROUPING")

    # print("CREATED GROUPNG: " + str(grouping))
    return grouping

"""population_size: int, mutation_rate: float, crossover_rate: float, fitness, mutations, create"""
def evolve(population_size, mutation_rate, elitism_rate, create_rate, crossover_rate, mutations):

    global best_grouping
    global best_fitness

    print("in evolve")
    population = [create() for _ in range(population_size)]
    population = list(map(lambda grouping: Individual(grouping, calculate_fitness(grouping)), population))

    gen = 0
    while gen < 200:
        # spawn next generation
        # print("Start of gen {}".format(gen))
        gen += 1
        population = spawn(population, mutation_rate, elitism_rate, create_rate, crossover_rate, mutations)
        population = list(map(lambda grouping: Individual(grouping, calculate_fitness(grouping)), population))

        dupl = False
        for ind in population:
            seen = set()
            for group in ind.grouping:
                for student in group:
                    if student in seen:
                        print("MAIN SCAN DUPLICATE")
                        print(ind)
                        dupl = True
                    seen.add(student)
        if dupl:
            exit()

        avg = 0
        for ind in population:
            avg += ind.fitness.value
        avg /= population_size
        print("AVG Fitness of gen {} is {}".format(gen, avg))

    print("Best grouping: " + str(best_grouping))
    print_grouping(best_grouping)
    print("Best fitness: " + str(best_fitness))


def crossover(individual_one, individual_two):

    grouping_one = individual_one.grouping[:]
    grouping_two = individual_two.grouping[:]

    # print("crossing {} with {}".format(grouping_one, grouping_two))

    group_count = len(grouping_one)
    offspring = list()

    # add groups that appear in both groupings
    for one in grouping_one:
        for two in grouping_two:
            if set(one) == set(two):
                dupl = False
                for group in offspring:
                    for student in one:
                        if student in group:
                            dupl = True
                            break
                    if dupl:
                        break
                if not dupl:
                    offspring.append(one)

    # print("added equals: {}".format(offspring))

    # step through groupings one and two, adding a whole group when possible to offspring. alternate between groupings after every successful addition
    on_one = True
    index_one = 0
    index_two = 0
    while index_one < len(grouping_one) or index_two < len(grouping_two):
        if on_one and index_one < len(grouping_one):
            dupl = False
            for student in grouping_one[index_one]:
                for group in offspring:
                    if student in group:
                        dupl = True
                        break
                if dupl:
                    break
            if not dupl:
                offspring.append(grouping_one[index_one])
                # print("appending {} from one".format(grouping_one[index_one]))
                del grouping_one[index_one]
                on_one = False
            else:
                index_one += 1
        elif on_one:
            on_one = False
        elif not on_one and index_two < len(grouping_two):
            dupl = False
            for student in grouping_two[index_two]:
                for group in offspring:
                    if student in group:
                        dupl = True
                        break
                if dupl:
                    break
            if not dupl:
                offspring.append(grouping_two[index_two])
                # print("appending {} from two".format(grouping_two[index_two]))
                del grouping_two[index_two]
                on_one = True
            else:
                index_two += 1
        elif not on_one:
            on_one = True

    # print("Finished appending all possible, list: {}".format(offspring))

    num_groups_so_far = len(offspring)
    num_groups_left = group_count - num_groups_so_far

    # remove students alread grouped again
    students_to_group = workbook.STUDENTS[:]
    for group in offspring:
        for student in group:
            students_to_group.remove(student)

    # print("Remaining: {}".format(students_to_group))

    # initialize groups for remainder groups
    remaining = list()

    for _ in range(num_groups_left):
        remaining.append(list())

    for index, student in enumerate(students_to_group):
        remaining[index % num_groups_left].append(student)

    for group in remaining:
        offspring.append(group)

    if len(offspring) != group_count:
        print("CROSSED OVER GROUPING NOT SAME SIZE")

    return offspring


def mutate(mutations, grouping: List[List[Student]]):
    """Mutate a grouping with a randomly chosen mutation."""
    return random.choice(mutations)(grouping)


def spawn(prev_population: List[Individual], mutation_rate: float, elitism_rate: float, create_rate: float, crossover_rate: float, mutations):
    count = len(prev_population)

    next_population = list()

    elite_count = math.floor(count * elitism_rate)
    create_count = math.floor(count * create_rate)
    crossover_count = count - elite_count - create_count

    for _ in range(elite_count):
        toap = select(prev_population).grouping
        # print("appending {}".format(toap))
        seen = set()
        dupl = False
        for group in toap:
            for student in group:
                if student in seen:
                    print("DUPLICATE")
                    print(toap)
                    dupl = True
                seen.add(student)
        if dupl:
            print("GOT DUPLICATE FROM ELITE")
            exit()
        next_population.append(toap)

    for _ in range(create_count):
        toap = create()
        # print("appending {}".format(toap))
        seen = set()
        dupl = False
        for group in toap:
            for student in group:
                if student in seen:
                    print("DUPLICATE")
                    print(toap)
                    dupl = True
                seen.add(student)
        if dupl:
            print("GOT DUPLICATE FROM CREATE")
            exit()
        next_population.append(toap)

    for _ in range(crossover_count):
        parent_one = select(prev_population)
        parent_two = select(prev_population)
        toap = crossover(parent_one, parent_two)
        # print("appending {}".format(toap))
        seen = set()
        dupl = False
        for group in toap:
            for student in group:
                if student in seen:
                    print("DUPLICATE")
                    print(toap)
                    dupl = True
                seen.add(student)
        if dupl:
            print("GOT DUPLICATE FROM CROSSOVER")
            exit()
        next_population.append(toap)

    for i, ind in enumerate(next_population):
        r = random.random()
        if r < mutation_rate:
            next_population[i] = mutate(mutations, ind)
            seen = set()
            dupl = False
            for group in next_population[i]:
                for student in group:
                    if student in seen:
                        print("DUPLICATE")
                        print(next_population[i])
                        dupl = True
                    seen.add(student)
            if dupl:
                print("GOT DUPLICATE FROM MUTATE")
                exit()
    return next_population


def select(population: List[Individual]):
    """Select random individuals from population and find most fit tournament-style."""
    SELECT_NUMBER = 8 #math.floor(len(population) / 3)
    selected = random.sample(population, SELECT_NUMBER)
    while len(selected) > 1:
        individual_one = selected.pop(0)
        individual_two = selected.pop(0)
        if (individual_one.fitness > individual_two.fitness):
            selected.append(individual_one)
        else:
            selected.append(individual_two)
    return selected[0]


def calculate_fitness(grouping: List[List[Student]]):

    global best_grouping
    global best_fitness

    # STUDENT PREFERENCES
    preferences_count = 0
    for group in grouping:
        for student in group:
            preferences_count += len(student.preferences)

    preferences_respected = 0
    for group in grouping:
        for student in group:
            for other in group:
                if other.email in student.preferences:
                    preferences_respected += 1

    preferences_value = preferences_respected / preferences_count  # 0 to 1

    # SKILL BALANCE, measured by the coefficient of variation of skills across group
    # Reference: http://www.statisticshowto.com/probability-and-statistics/how-to-find-a-coefficient-of-variation/
    # e.g. group = [[1, 2, 3, 4, 5],
    #               [1, 2, 3, 4, 5]]
    #  group_skills = [1, 2, 3, 4, 5]
    #  group_skill_avg = 3
    #  group_skill_std = 1.41
    #  group_skills_coef = 1.41 / 3 = 0.47

    if len(grouping) < 1:
        print("GROUPING IS TOO SMALL")
        print(grouping)
    for group in grouping:
        if len(group) < 1:
            print("GROUP IS TOO SMALL")
            print(grouping)


    skills_by_group = []
    for _ in range(len(grouping)):
        skills_by_group += [[0] * len(grouping[0][0].skills)]  # assumes there is at least one student in one group

    for group_index, group in enumerate(grouping):
        skills_within_group = [0] * len(group[0].skills)
        for student in group:
            for skill_index, skill in enumerate(student.skills):
                skills_within_group[skill_index] += skill
        for skill_total in skills_within_group:
            skill_total = skill_total / len(group)  # get average
        skills_by_group[group_index] = skills_within_group

    skills_coef_by_group = list()
    for skills in skills_by_group:
        # print("skills: " + str(skills))
        # print("mean of skills: " + str(np.mean(skills)))
        # print("stdev of skills: " + str(np.std(skills)))
        skills_coef_by_group.append(np.std(skills) / np.mean(skills))

    balance_value = 1 - np.mean(skills_coef_by_group)

    # SKILL FAIRNESS, measured by the coefficient of variation of skills across grouping
    #  e.g. group_1_skills = [1, 2, 3, 4, 5]
    #       group_2_skills = [5, 4, 3, 2, 1]
    #       grouping_skills_avg = [3, 3, 3, 3, 3]
    #       grouping_skills_std = [2, 1, 0, 1, 2]
    #       grouping_coef = [(2/3), (1/3), (0/3), (1/3), (2/3)]
    #       grouping_coef_avg = 0.396

    # transpose the list of lists
    skills_by_group_transposed = list(map(list, zip(*skills_by_group)))
    skills_coef_by_grouping = list()
    for skills in skills_by_group_transposed:
        skills_coef_by_grouping.append(np.std(skills) / np.mean(skills))

    fairness_value = 1 - np.mean(skills_coef_by_grouping)

    current_fitness = Fitness(preferences_value, balance_value, fairness_value)
    if current_fitness > best_fitness:
        best_fitness = current_fitness
        best_grouping = grouping

    return current_fitness


def print_grouping(grouping):
    for index, group in enumerate(grouping):
        print("Group " + str(index) + "\n")
        for student in group:
            print(student)
