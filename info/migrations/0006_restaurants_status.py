# Generated by Django 3.1 on 2020-08-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20200814_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]
