# Generated by Django 3.1.6 on 2021-02-09 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_thoughts_pub_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Thoughts',
            new_name='Thought',
        ),
        migrations.RenameField(
            model_name='thought',
            old_name='thoughts_text',
            new_name='thought_text',
        ),
    ]
