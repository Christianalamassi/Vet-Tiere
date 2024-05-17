# Generated by Django 3.2.25 on 2024-05-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20240515_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='time',
            field=models.CharField(choices=[('10:00', '10:00'), ('8:00', '8:00'), ('11:00', '11:00'), ('09:00', '9:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00')], max_length=7),
        ),
    ]