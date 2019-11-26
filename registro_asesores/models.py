# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AsesoresDb(models.Model):
    cod_asesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=154, blank=True, null=True)
    ciudad = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='ciudad', blank=True, null=True, related_name='AsesoresDb.ciudad+')
    direccion2 = models.CharField(max_length=154, blank=True, null=True)
    ciudad2 = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='ciudad2', blank=True, null=True, related_name='AsesoresDb.ciudad2+')
    celular = models.CharField(max_length=15, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    t_asesor = models.CharField(max_length=15, blank=True, null=True)
    comision = models.ForeignKey('Comisiones', models.DO_NOTHING, db_column='comision', blank=True, null=True)
    cedula = models.CharField(max_length=15, blank=True, null=True)
    c_cedula = models.CharField(max_length=150, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fecha_s = models.DateField(blank=True, null=True)
    perfil = models.IntegerField(blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    fechaexpedicion = models.DateField(db_column='fechaExpedicion', blank=True, null=True)  # Field name made lowercase.
    ciudadexpedicion = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='ciudadExpedicion', blank=True, null=True, related_name='AsesoresDb.ciudadexpedicion+')  # Field name made lowercase.
    genero = models.ForeignKey('Genero', models.DO_NOTHING, db_column='genero')

    class Meta:
        managed = True
        db_table = 'asesores_db'


class Municipio(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_dane = models.CharField(max_length=15)
    departamento = models.CharField(max_length=18)
    municipio = models.CharField(max_length=27)

    class Meta:
        managed = False
        db_table = 'municipio'
    
    def __str__(self):
        return self.municipio


class Perfilasesor(models.Model):
    codigo = models.AutoField(primary_key=True)
    perfil = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'perfilasesor'

    def __str__(self):
        return self.perfil


class Genero(models.Model):
    codigo = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'genero'

    def __str__(self):
        return self.genero

class Comisiones(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=20, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comisiones'

    def __str__(self):
        return self.tipo
