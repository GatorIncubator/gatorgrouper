""" This file is used to create all the models for Django """
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class Professor(AbstractUser):
    """ Model showcasing the Professors """

    REQUIRED_FIELDS = ("first_name", "last_name")
    USERNAME_FIELD = "email"
    username = None
    email = models.EmailField(max_length=200, unique=True)
    professor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    objects = UserManager()

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Semester_Class(models.Model):
    """ Model showcasing the list of the semesters followed by the classes """

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


class Assignment(models.Model):
    """ Model showcasing the list of assignments and the description """

    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    assignment_id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(Semester_Class, on_delete=models.CASCADE)
    assignment_name = models.CharField(max_length=30, default="Group Project")
    description = models.CharField(max_length=350, blank=True)

    def __str__(self):
        return "{}: {}".format(self.class_id, self.assignment_name)


class Student(models.Model):
    """ Model showcasing the list of students in the class """

    class_id = models.ForeignKey(Semester_Class, on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Grouped_Student(models.Model):
    """ Model showcasing the grouped students """

    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=30, default="group #")

    def __str__(self):
        return "{}: {}".format(self.group_name, self.student_id)

    # pylint: disable=too-few-public-methods
    class Meta:
        """ will be used to enforce unique contraint between assignment_id and student_id """

        unique_together = ("assignment_id", "student_id")


class Student_Conflict(models.Model):
    """ Model with severity ranking for student 1 and student 2 """

    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SEVERITY_CHOICES = ((ONE, "1"), (TWO, "2"), (THREE, "3"), (FOUR, "4"), (FIVE, "5"))
    conflict_id = models.AutoField(primary_key=True)
    student1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="id1", blank=True
    )
    student2 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="id2", blank=True
    )
    severity_rank = models.CharField(max_length=1, choices=SEVERITY_CHOICES, blank=True)
    class_id = models.ForeignKey(Semester_Class, on_delete=models.CASCADE, blank=True)
