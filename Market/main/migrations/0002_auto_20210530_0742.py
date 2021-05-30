# Generated by Django 3.2.3 on 2021-05-30 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Идентификатор'),
        ),
    ]
