# Generated by Django 3.2.25 on 2024-05-15 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20240515_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='time',
            field=models.CharField(choices=[('14:00', '14:00'), ('13:00', '13:00'), ('12:00', '12:00'), ('09:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('8:00', '8:00')], max_length=7),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]