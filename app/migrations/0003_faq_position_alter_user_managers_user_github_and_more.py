# Generated by Django 5.0.6 on 2024-07-23 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_service_alter_user_email_alter_user_username"),
    ]

    operations = [
        migrations.CreateModel(
            name="FAQ",
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
                ("question", models.TextField()),
                ("answer", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Position",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "mode",
                    models.CharField(
                        choices=[
                            ("remote", "remote"),
                            ("on-site", "on-site"),
                            ("hybrid", "hybrid"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("full-time", "full-time"),
                            ("part-time", "part-time"),
                            ("contract", "contract"),
                            ("internship", "internship"),
                        ],
                        max_length=255,
                    ),
                ),
                ("salary", models.PositiveIntegerField(blank=True, null=True)),
                ("is_open", models.BooleanField(default=True)),
                ("open_from", models.DateField(blank=True, null=True)),
                ("open_to", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.AddField(
            model_name="user",
            name="github",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="pic",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.CreateModel(
            name="Message",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=13)),
                ("message", models.TextField()),
                (
                    "service",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.service",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="position",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.position",
            ),
        ),
    ]
