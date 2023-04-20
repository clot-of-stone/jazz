# Generated by Django 4.1.7 on 2023-04-10 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0004_remove_student_teacher"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentTeacher",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="positions",
                        to="school.student",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="positions",
                        to="school.teacher",
                    ),
                ),
            ],
        ),
    ]