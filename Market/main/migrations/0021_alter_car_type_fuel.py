# Generated by Django 3.2.3 on 2021-06-26 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='type_fuel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.typefuel'),
        ),
    ]