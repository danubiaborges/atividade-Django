# Generated by Django 4.2.2 on 2023-06-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ItaCar_app', '0002_remove_movimento_conta_delete_contacomum_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCorrida', models.IntegerField()),
                ('nomePass', models.CharField(max_length=255)),
                ('nota', models.IntegerField()),
                ('comentario', models.TextField()),
            ],
        ),
    ]
