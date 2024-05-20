# Generated by Django 5.0.3 on 2024-05-20 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0029_djangorestframeworkdetails"),
    ]

    operations = [
        migrations.AddField(
            model_name="git",
            name="code_block",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pythonmeaning",
            name="code_block",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pythonotherimportantlibraries",
            name="code_block",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="randomquestions",
            name="code_block",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="randomquestions",
            name="pdf",
            field=models.FileField(blank=True, upload_to="testing_pdfs"),
        ),
        migrations.AddField(
            model_name="randomquestions",
            name="url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sqldetails",
            name="code_block",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sqlquestions",
            name="code_block",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="testing",
            name="code_block",
            field=models.TextField(blank=True, null=True),
        ),
    ]