# Generated by Django 4.0.5 on 2022-07-03 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_alter_userdetail_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='referral_logic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referred_vistor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor', to=settings.AUTH_USER_MODEL)),
                ('user_referring', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]