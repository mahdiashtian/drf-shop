# Generated by Django 4.0.4 on 2022-06-03 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_alter_comment_father'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='father',
            new_name='son',
        ),
    ]
