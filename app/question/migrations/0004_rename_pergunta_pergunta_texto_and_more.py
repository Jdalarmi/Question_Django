# Generated by Django 4.2.9 on 2024-01-11 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_rename_texto_pergunta_pergunta_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pergunta',
            old_name='pergunta',
            new_name='texto',
        ),
        migrations.RemoveField(
            model_name='resposta',
            name='texto_resposta',
        ),
        migrations.AddField(
            model_name='resposta',
            name='pergunta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='question.pergunta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resposta',
            name='resposta',
            field=models.CharField(max_length=250),
        ),
    ]
