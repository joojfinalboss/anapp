# Generated by Django 5.0.1 on 2024-03-31 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bode', '0004_pecaavulsa_valor_metro_quadrado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pecaavulsa',
            name='movel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bode.movel'),
            preserve_default=False,
        ),
    ]
