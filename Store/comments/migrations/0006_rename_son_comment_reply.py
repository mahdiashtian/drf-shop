# Generated by Django 4.0.4 on 2022-06-03 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_rename_father_comment_son'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='son',
            new_name='reply',
        ),
    ]