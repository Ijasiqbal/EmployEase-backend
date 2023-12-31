# Generated by Django 4.2.6 on 2023-10-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='manager_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='date_of_joining',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='years_of_experience',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
