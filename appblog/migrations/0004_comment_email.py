# Generated by Django 4.2 on 2023-05-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0003_comment_comment_appblog_com_created_9d1803_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='test1@ex.com', max_length=254),
            preserve_default=False,
        ),
    ]
