# Generated by Django 5.2.3 on 2025-07-11 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_stud_lang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stud',
            name='lang',
        ),
    ]
