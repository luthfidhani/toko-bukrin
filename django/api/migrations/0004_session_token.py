# Generated by Django 3.2.9 on 2021-11-11 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0003_alter_session_expired_at")]

    operations = [
        migrations.AddField(
            model_name="session",
            name="token",
            field=models.CharField(max_length=255, null=True),
        )
    ]
