# Generated by Django 4.0.4 on 2022-06-02 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_alter_comment_options_comment_main_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='father',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.comment', verbose_name='ریپلای شده'),
        ),
    ]