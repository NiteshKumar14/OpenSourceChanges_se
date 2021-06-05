# Generated by Django 3.2 on 2021-05-30 03:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('natter', '0003_auto_20210529_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouproom',
            name='auth_token',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grouproom',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grouproom',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
