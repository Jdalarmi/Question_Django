# Generated by Django 4.2.9 on 2024-01-11 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_rename_pergunta_pergunta_texto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resposta',
            old_name='resposta',
            new_name='texto',
        ),
    ]
