# Generated by Django 2.2b1 on 2019-03-13 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("gatorgrouper", "0001_initial")]

    operations = [
        migrations.AlterUniqueTogether(
            name="grouped_student", unique_together={("assignment_id", "student_id")}
        )
    ]