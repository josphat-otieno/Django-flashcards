# Generated by Django 3.2.5 on 2021-07-21 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcardApp', '0002_flashcard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcard',
            name='flash_image',
        ),
    ]
