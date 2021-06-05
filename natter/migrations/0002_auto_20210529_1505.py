# Generated by Django 3.2 on 2021-05-29 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouproom',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='grouproom',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='grouproom',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='grouproom',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
