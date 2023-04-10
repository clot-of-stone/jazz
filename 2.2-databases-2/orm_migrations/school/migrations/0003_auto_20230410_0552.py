from django.db import models, migrations


def forward(apps, schema_editor):
    Student = apps.get_model('school', 'Student')
    for student in Student.objects.all():
        student.teachers.add(student.teacher)


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_student_teachers_alter_student_group_and_more'),
    ]

    operations = [
        migrations.RunPython(forward)
    ]