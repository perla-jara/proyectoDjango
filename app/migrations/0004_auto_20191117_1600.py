# Generated by Django 2.2.6 on 2019-11-17 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191101_2114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'permissions': (('administrador', 'Es administrador'), ('cliente', 'Es cliente'))},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'permissions': (('administrador', 'Es administrador'), ('cliente', 'Es cliente'))},
        ),
    ]
