# Generated by Django 4.2.9 on 2024-01-11 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_rename_texto_resposta_texto_resposta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pergunta',
            old_name='texto',
            new_name='pergunta',
        ),
        migrations.RenameField(
            model_name='resposta',
            old_name='pergunta',
            new_name='resposta',
        ),
    ]
