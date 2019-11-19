# Generated by Django 2.2.6 on 2019-11-19 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsesoresDb',
            fields=[
                ('cod_asesor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('apellido', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=154, null=True)),
                ('direccion2', models.CharField(blank=True, max_length=154, null=True)),
                ('celular', models.CharField(blank=True, max_length=15, null=True)),
                ('mail', models.CharField(blank=True, max_length=50, null=True)),
                ('t_asesor', models.CharField(blank=True, max_length=15, null=True)),
                ('cedula', models.CharField(blank=True, max_length=15, null=True)),
                ('c_cedula', models.CharField(blank=True, max_length=150, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('fecha_s', models.DateField(blank=True, null=True)),
                ('perfil', models.IntegerField(blank=True, null=True)),
                ('fechanacimiento', models.DateField(blank=True, db_column='fechaNacimiento', null=True)),
                ('fechaexpedicion', models.DateField(blank=True, db_column='fechaExpedicion', null=True)),
            ],
            options={
                'db_table': 'asesores_db',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comisiones',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=15, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=20, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comisiones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DbAbogados',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=51)),
                ('apellidos', models.CharField(blank=True, max_length=45, null=True)),
                ('cedula', models.IntegerField(blank=True, null=True)),
                ('tarjeta_p', models.IntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=154, null=True)),
                ('ciudadnombre', models.CharField(blank=True, db_column='ciudadNombre', max_length=27, null=True)),
                ('departamento', models.CharField(blank=True, max_length=18, null=True)),
                ('direccion2', models.CharField(blank=True, max_length=154, null=True)),
                ('empresa', models.CharField(blank=True, max_length=56, null=True)),
                ('celular2', models.CharField(blank=True, max_length=15, null=True)),
                ('celular1', models.CharField(blank=True, max_length=15, null=True)),
                ('celular', models.CharField(blank=True, max_length=15, null=True)),
                ('fijo2', models.CharField(blank=True, max_length=15, null=True)),
                ('fijo1', models.CharField(blank=True, max_length=15, null=True)),
                ('fijo', models.CharField(blank=True, max_length=15, null=True)),
                ('fax', models.CharField(blank=True, max_length=15, null=True)),
                ('e_mail1', models.CharField(blank=True, max_length=67, null=True)),
                ('e_mail2', models.CharField(blank=True, max_length=67, null=True)),
                ('contacto', models.IntegerField(blank=True, null=True)),
                ('fecha_actualizacion', models.DateField(blank=True, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=150, null=True)),
                ('copiacc', models.CharField(blank=True, db_column='copiaCc', max_length=150, null=True)),
                ('copiatp', models.CharField(blank=True, db_column='copiaTp', max_length=150, null=True)),
                ('fechaexpedicion', models.DateField(blank=True, db_column='fechaExpedicion', null=True)),
            ],
            options={
                'db_table': 'db_abogados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
                ('abreviatura', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'genero',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_dane', models.CharField(max_length=15)),
                ('departamento', models.CharField(max_length=18)),
                ('municipio', models.CharField(max_length=27)),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('perfil', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'perfil',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('actividad', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('reprogramar', models.DateField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'seguimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subitemseguimiento',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('subsegumiento', models.CharField(db_column='subSegumiento', max_length=30)),
            ],
            options={
                'db_table': 'subitemseguimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoSeguimiento',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('seguimiento', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tipo_seguimiento',
                'managed': False,
            },
        ),
    ]
