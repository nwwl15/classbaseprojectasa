# Generated by Django 4.0.5 on 2022-07-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_userdetail_non_withdrawal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='ids',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
