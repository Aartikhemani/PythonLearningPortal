# Generated by Django 5.0.3 on 2024-04-24 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0026_djangolibrary"),
    ]

    operations = [
        migrations.AddField(
            model_name="djangorestframework",
            name="code_block",
            field=models.TextField(blank=True, null=True),
        ),
    ]