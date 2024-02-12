# Generated by Django 5.0.1 on 2024-02-11 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_course_course_date_created_and_more"),
        ("users", "0006_cohormember"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClassSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "description",
                    models.TextField(blank=True, max_length=1000, null=True),
                ),
                ("start_date_and_time", models.DateTimeField()),
                ("end_date_and_time", models.DateTimeField()),
                ("is_repeated", models.BooleanField(default=False)),
                ("repeat_frequency", models.IntegerField(default=1)),
                ("is_active", models.BooleanField(default=True)),
                ("organizer", models.CharField(max_length=255)),
                ("venue", models.CharField(max_length=255)),
                (
                    "cohort",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.cohort"
                    ),
                ),
            ],
        ),
    ]