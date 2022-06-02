# Generated by Django 4.0.4 on 2022-06-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'base_manager_name': 'objects', 'ordering': ['date_time_added', 'date_time_edit'], 'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AddField(
            model_name='comment',
            name='main_message',
            field=models.CharField(default='fsdf', max_length=150, verbose_name='کامنت'),
            preserve_default=False,
        ),
    ]