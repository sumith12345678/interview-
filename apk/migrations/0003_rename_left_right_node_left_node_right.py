# Generated by Django 4.2.1 on 2023-05-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0002_node_left_right'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='left_right',
            new_name='left',
        ),
        migrations.AddField(
            model_name='node',
            name='right',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]