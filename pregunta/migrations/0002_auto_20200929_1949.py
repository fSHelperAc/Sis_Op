# Generated by Django 3.0.3 on 2020-09-29 17:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pregunta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='resp_c',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='respuesta_a',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='respuesta_b',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='respuesta_c',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='author',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pregunta',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('es_correcta', models.BooleanField(default=False)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuesta', to='pregunta.Pregunta')),
            ],
        ),
    ]
