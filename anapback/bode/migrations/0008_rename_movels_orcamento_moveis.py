# Generated by Django 5.0.1 on 2024-03-31 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bode', '0007_orcamento_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orcamento',
            old_name='movels',
            new_name='moveis',
        ),
    ]