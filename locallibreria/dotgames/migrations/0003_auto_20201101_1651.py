# Generated by Django 3.1.2 on 2020-11-01 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dotgames', '0002_auto_20201031_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dotgames.autor'),
        ),
    ]
