# Generated by Django 5.0.1 on 2024-01-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0002_alter_section_section_name_alter_student_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
