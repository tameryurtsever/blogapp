# Generated by Django 3.2.5 on 2021-07-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_context',
            new_name='comment_content',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
