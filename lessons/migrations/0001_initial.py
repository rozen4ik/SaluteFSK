# Generated by Django 4.1.2 on 2022-10-05 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=300, verbose_name='секция')),
                ('device_id', models.CharField(max_length=150, verbose_name='номер устройства')),
                ('trener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='тренер')),
            ],
            options={
                'verbose_name': 'занятия',
                'verbose_name_plural': 'занятия',
            },
        ),
    ]
