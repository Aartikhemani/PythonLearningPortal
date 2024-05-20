# Generated by Django 5.0.3 on 2024-04-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0025_djangorestframework_alter_git_img_alter_git_img2_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DjangoLibrary",
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
                ("title", models.CharField(blank=True, max_length=355)),
                ("text", models.TextField(blank=True)),
                ("question", models.TextField(blank=True, max_length=255)),
                ("answer", models.TextField(blank=True)),
                (
                    "img",
                    models.ImageField(blank=True, upload_to="productImages/Django"),
                ),
                (
                    "img2",
                    models.ImageField(blank=True, upload_to="productImages/Django"),
                ),
                (
                    "img3",
                    models.ImageField(blank=True, upload_to="productImages/Django"),
                ),
                ("url", models.URLField(blank=True, null=True)),
                ("pdf", models.FileField(blank=True, upload_to="pdfs/Django")),
            ],
        ),
    ]