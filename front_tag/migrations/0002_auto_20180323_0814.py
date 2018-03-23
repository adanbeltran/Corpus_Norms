# Generated by Django 2.0.3 on 2018-03-23 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front_tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atributo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_parametro', models.TextField()),
                ('atributo_id', models.BigIntegerField(db_index=True, default=0)),
                ('orden', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('etiqueta_text', models.CharField(max_length=10000)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('activa', models.BooleanField(default=True, verbose_name='Estado de Etiqueta')),
            ],
        ),
        migrations.CreateModel(
            name='Etiquetado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('valor_parametro', models.TextField()),
                ('version', models.BigIntegerField()),
                ('orden', models.BigIntegerField(default=0)),
                ('etiqueta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front_tag.Etiqueta')),
            ],
        ),
        migrations.CreateModel(
            name='Norma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('norm_text', models.CharField(max_length=10000)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('norm_url', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='etiquetado',
            name='norma_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front_tag.Norma'),
        ),
        migrations.AddField(
            model_name='atributo',
            name='etiqueta_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front_tag.Etiqueta'),
        ),
    ]