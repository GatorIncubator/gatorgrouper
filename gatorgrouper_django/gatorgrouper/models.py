from django.db import models

# Create your models here.
class Professor(models.Model):
    email = models.EmailField(max_length = 200)
    professor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)

    def __str__(self):
        return '{}'.format(self.email)


class Semester_Class(models.Model):
    professor_id = models.ForeignKey(
            Professor,
            on_delete=models.CASCADE,
            )
    semester = models.CharField(max_length = 50)
    class_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length = 10)
    class_number = models.CharField(max_length = 10)
    class_section = models.CharField(max_length = 10)

    def __str__(self):
        return '{}: {}*{}'.format(self.department, self.class_number, self.class_section)


class Assignments(models.Model):
    class_id = models.ForeignKey(
            Semester_Class,
            on_delete=models.CASCADE,
            )
    assignment_id = models.CharField(max_length = 20, primary_key = True)
    description = models.CharField(max_length = 250)

    def __str__(self):
        return '{}'.format(self.assignment_id)

class Students(models.Model):
    class_id = models.ForeignKey(
            Semester_Class,
            on_delete=models.CASCADE,
            )
    student_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)

class Grouped_Students(models.Model):
    assignment_id = models.ForeignKey(
            Assignments,
            on_delete=models.CASCADE,
            )
    student_id = models.ForeignKey(
            Students,
            on_delete=models.CASCADE,
            )
    group_id = models.CharField(max_length = 40)

    def __str__(self):
        return '{}: {}'.format(self.assignment_id, self.group_id)
