# Generated by Django 3.2.11 on 2022-01-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='my_leads',
            field=models.ManyToManyField(to='lead.Leads', verbose_name='My Leads'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(max_length=9, unique=True, verbose_name='Phone number'),
        ),
    ]
