# Generated by Django 4.1.2 on 2022-10-22 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.functions


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=utils.functions.generate_random_otp)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='otp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
