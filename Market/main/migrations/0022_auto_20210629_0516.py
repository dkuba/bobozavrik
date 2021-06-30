# Generated by Django 3.2.3 on 2021-06-29 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),

        ('admin', '0003_logentry_add_action_flag_choices'),

        ('main', '0021_alter_car_type_fuel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.AlterModelManagers(
            name='profile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='services',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='stuff',
            name='seller',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
