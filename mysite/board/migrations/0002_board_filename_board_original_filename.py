# Generated by Django 5.1.4 on 2024-12-06 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="filename",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="파일명"
            ),
        ),
        migrations.AddField(
            model_name="board",
            name="original_filename",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="원본파일명"
            ),
        ),
    ]