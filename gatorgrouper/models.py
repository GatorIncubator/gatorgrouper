""" This is undocumented """
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Professor(models.Model):
    """ This is undocumented """

    email = models.EmailField(max_length=200)
    professor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Semester_Class(models.Model):
    """ This is undocumented """

    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    SPRING_2019 = "S19"
    FALL_2019 = "F19"
    SEMESTER_CHOICES = ((SPRING_2019, "Spring, 2019"), (FALL_2019, "Fall, 2019"))
    semester = models.CharField(
        max_length=3, choices=SEMESTER_CHOICES, default="---------"
    )
    class_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=10)
    class_number = models.CharField(max_length=10)
    class_section = models.CharField(max_length=10)
    domain_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "{}: {}*{}".format(
            self.department, self.class_number, self.class_section
        )


class Assignments(models.Model):
    """ This is undocumented """

    class_id = models.ForeignKey(Semester_Class, on_delete=models.CASCADE)
    assignment_id = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return "{}".format(self.assignment_id)


class Students(models.Model):
    """ This is undocumented """
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Semester_Class, on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Grouped_Students(models.Model):
    """ This is undocumented """

    assignment_id = models.ForeignKey(Assignments, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    group_id = models.CharField(max_length=40)

    def __str__(self):
        return "{}: {}".format(self.assignment_id, self.group_id)

class Student_Reviews(models.Model):
    """
    Model containing the data from the survey form
    given after a grouping has completed
    """
    question_one = models.IntegerField(min_value=1, max_value=5)
    question_two = models.IntegerField(min_value=1, max_value=5)
    question_three = models.IntegerField(min_value=1, max_value=5)
    question_four = models.IntegerField(min_value=1, max_value=5)
    question_five = models.IntegerField(min_value=1, max_value=5)
    question_six = models.TextField(max_length=1000)
    # need to change booleanfield to integerfield if quest. seven is changed to
    # radio button (reccommended)
    question_seven = models.BooleanField()

    #TODO: set up model to accept data from form
    #option1 = models.AutoField()
    #option2 = models.AutoField()
    #option3 = models.AutoField()
    #option4 = models.AutoField()
    #option5 = models.AutoField()
