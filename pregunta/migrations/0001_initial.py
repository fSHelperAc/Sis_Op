# Generated by Django 3.0.3 on 2020-09-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta_s', models.CharField(max_length=255)),
                ('respuesta_a', models.CharField(max_length=255)),
                ('respuesta_b', models.CharField(max_length=255)),
                ('respuesta_c', models.CharField(max_length=255)),
                ('resp_c', models.CharField(max_length=100)),
            ],
        ),
    ]
