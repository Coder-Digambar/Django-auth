# Generated by Django 5.2.3 on 2025-07-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='', max_length=300, upload_to='book/cover'),
        ),
        migrations.AlterField(
            model_name='book',
            name='docs',
            field=models.FileField(default='', max_length=300, upload_to='book/docs'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
