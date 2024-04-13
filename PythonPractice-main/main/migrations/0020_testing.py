# Generated by Django 5.0.3 on 2024-03-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0019_pythonotherimportantlibraries"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testing",
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
                ("title", models.CharField(blank=True, max_length=225)),
                ("text", models.TextField()),
                ("img", models.ImageField(blank=True, upload_to="testingImages")),
                ("url", models.URLField(blank=True, null=True)),
                ("pdf", models.FileField(blank=True, upload_to="testing_pdfs")),
            ],
        ),
    ]