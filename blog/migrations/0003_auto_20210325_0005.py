# Generated by Django 3.0.5 on 2021-03-24 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210325_0001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_title',
            new_name='title',
        ),
    ]