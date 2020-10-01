# Generated by Django 3.1.1 on 2020-10-01 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6)),
                ('descriptions', models.TextField(max_length=256)),
                ('raiting', models.DecimalField(decimal_places=1, max_digits=1)),
            ],
        ),
    ]