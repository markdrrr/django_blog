# Generated by Django 3.1.1 on 2020-09-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
