# Generated by Django 4.0.5 on 2022-07-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_referral_logic_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='withdrawal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]