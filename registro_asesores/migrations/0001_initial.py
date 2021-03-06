# Generated by Django 2.2.6 on 2019-11-26 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='Perfilasesor',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('perfil', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'perfilasesor',
                'managed': False,
            },
        ),
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
                ('ciudad', models.ForeignKey(blank=True, db_column='ciudad', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='AsesoresDb.ciudad+', to='registro_asesores.Municipio')),
                ('ciudad2', models.ForeignKey(blank=True, db_column='ciudad2', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='AsesoresDb.ciudad2+', to='registro_asesores.Municipio')),
                ('ciudadexpedicion', models.ForeignKey(blank=True, db_column='ciudadExpedicion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='AsesoresDb.ciudadexpedicion+', to='registro_asesores.Municipio')),
                ('comision', models.ForeignKey(blank=True, db_column='comision', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='registro_asesores.Comisiones')),
                ('genero', models.ForeignKey(db_column='genero', on_delete=django.db.models.deletion.DO_NOTHING, to='registro_asesores.Genero')),
            ],
            options={
                'db_table': 'asesores_db',
                'managed': True,
            },
        ),
    ]
