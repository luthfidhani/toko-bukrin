# Generated by Django 3.2.9 on 2021-11-11 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="session", name="is_active", field=models.BooleanField(default=1)
        )
    ]
