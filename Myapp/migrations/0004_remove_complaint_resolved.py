# Generated by Django 5.1.3 on 2024-12-22 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_rename_student_payment_students_complaint_resolved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='resolved',
        ),
    ]