# Generated by Django 5.0.1 on 2024-01-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0002_avaliacao_delete_avaliacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
