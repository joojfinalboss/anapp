# Generated by Django 5.0.1 on 2024-03-30 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PecaAvulsa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('altura', models.FloatField()),
                ('largura', models.FloatField()),
                ('espessura', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PecaAvulsaPadrao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('altura', models.FloatField()),
                ('largura', models.FloatField()),
                ('espessura', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('movels', models.ManyToManyField(to='bode.movel')),
            ],
        ),
    ]
