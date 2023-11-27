# Generated by Django 4.2.7 on 2023-11-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Capybaras",
            new_name="Capybara",
        ),
        migrations.AddField(
            model_name="location",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=5, max_digits=10, null=True
            ),
        ),
    ]
