# Generated by Django 4.2.1 on 2023-05-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='left_right',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
