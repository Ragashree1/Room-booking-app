# Generated by Django 4.1.7 on 2023-04-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roomBooking", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[("T", "Staff"), ("S", "Student")], max_length=1
            ),
        ),
    ]
