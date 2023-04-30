# Generated by Django 4.1.7 on 2023-04-29 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("roomBooking", "0003_room_alter_user_user_type_reservation_user_room"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reservation",
            name="end_time",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="start_time",
        ),
        migrations.RemoveField(
            model_name="room",
            name="id",
        ),
        migrations.RemoveField(
            model_name="user",
            name="room",
        ),
        migrations.AddField(
            model_name="reservation",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="reservation",
            name="time_slot",
            field=models.TimeField(default="09:00:00"),
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default="Kim", max_length=50),
        ),
        migrations.AlterField(
            model_name="room",
            name="name",
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AddConstraint(
            model_name="reservation",
            constraint=models.UniqueConstraint(
                fields=("room", "time_slot", "date"), name="room_time_slot_pk"
            ),
        ),
        
    ]