# Generated by Django 3.1.2 on 2020-11-01 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotgames', '0004_auto_20201101_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='autor',
        ),
        migrations.AlterField(
            model_name='autor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
