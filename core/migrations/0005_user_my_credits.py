# Generated by Django 3.2.11 on 2022-01-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='my_credits',
            field=models.IntegerField(default=0, verbose_name='Credits'),
        ),
    ]