# Generated by Django 5.2.1 on 2025-05-16 02:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudadano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_identificacion', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Ciudadano',
                'verbose_name_plural': 'Ciudadanos',
            },
        ),
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Segmento',
                'verbose_name_plural': 'Segmentos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TipoIdentificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo documento',
                'verbose_name_plural': 'Tipos de documentos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('nivel', models.CharField(db_index=True, default=1)),
                ('categoria_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoriapadre', to='gestion.categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversacion_id', models.CharField(max_length=250)),
                ('observacion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.categoria')),
                ('ciudadano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.ciudadano')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tipificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('segmento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.segmento')),
            ],
            options={
                'verbose_name': 'Tipificación',
                'verbose_name_plural': 'Tipificaciones',
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='categoria',
            name='tipificacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.tipificacion'),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='tipo_identificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.tipoidentificacion'),
        ),
        migrations.AddIndex(
            model_name='ciudadano',
            index=models.Index(fields=['numero_identificacion'], name='gestion_ciu_numero__1b4597_idx'),
        ),
    ]
