# Generated by Django 4.2.6 on 2023-10-27 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_department', '0005_alter_employee_yearsofexperience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
