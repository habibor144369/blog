# Generated by Django 3.0.5 on 2021-03-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210324_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='key',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
