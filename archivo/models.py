# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Municipio(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_dane = models.CharField(max_length=15)
    departamento = models.CharField(max_length=18)
    municipio = models.CharField(max_length=27)

    class Meta:
        managed = False
        db_table = 'municipio'


class DbAbogados(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=51)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    cedula = models.IntegerField(blank=True, null=True)
    tarjeta_p = models.IntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=154, blank=True, null=True)
    ciudad = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='ciudad', blank=True, null=True, related_name='DbAbogados.ciudad+')
    ciudadnombre = models.CharField(db_column='ciudadNombre', max_length=27, blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(max_length=18, blank=True, null=True)
    direccion2 = models.CharField(max_length=154, blank=True, null=True)
    ciudad2 = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='ciudad2', blank=True, null=True, related_name='DbAbogados.ciudad2+')
    perfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='perfil', blank=True, null=True)
    empresa = models.CharField(max_length=56, blank=True, null=True)
    celular2 = models.CharField(max_length=15, blank=True, null=True)
    celular1 = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    fijo2 = models.CharField(max_length=15, blank=True, null=True)
    fijo1 = models.CharField(max_length=15, blank=True, null=True)
    fijo = models.CharField(max_length=15, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)
    e_mail1 = models.CharField(max_length=67, blank=True, null=True)
    e_mail2 = models.CharField(max_length=67, blank=True, null=True)
    contacto = models.ForeignKey('OrigenContacto', models.DO_NOTHING, db_column='contacto', blank=True, null=True)
    fecha_actualizacion = models.DateField(blank=True, null=True)
    actualizacion = models.ForeignKey('AsesoresDb', models.DO_NOTHING, db_column='actualizacion', blank=True, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)
    fechaexpedicion = models.DateField(db_column='fechaExpedicion', blank=True, null=True)  # Field name made lowercase.
    ciudadexpedicion = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='ciudadExpedicion', blank=True, null=True, related_name='DbAbogados.ciudadexpedicion+')  # Field name made lowercase.
    genero = models.ForeignKey('Genero', models.DO_NOTHING, db_column='genero')

    class Meta:
        managed = False
        db_table = 'db_abogados'


class Perfil(models.Model):
    codigo = models.AutoField(primary_key=True)
    perfil = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'perfil'


class Genero(models.Model):
    codigo = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'genero'


class AsesoresDb(models.Model):
    cod_asesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=154, blank=True, null=True)
    ciudad = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='ciudad', blank=True, null=True, related_name='AsesoresDb.ciudad+')
    direccion2 = models.CharField(max_length=154, blank=True, null=True)
    ciudad2 = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='ciudad2', blank=True, null=True, related_name='AsesoresDb.ciudad2+')
    celular = models.CharField(max_length=15, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    t_asesor = models.CharField(max_length=15, blank=True, null=True)
    comision = models.ForeignKey('Comisiones', models.DO_NOTHING, db_column='comision', blank=True, null=True)
    cedula = models.CharField(max_length=15, blank=True, null=True)
    c_cedula = models.CharField(max_length=150, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fecha_s = models.DateField(blank=True, null=True)
    perfil = models.ForeignKey('Perfilasesor', models.DO_NOTHING, db_column='perfil', blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    fechaexpedicion = models.DateField(db_column='fechaExpedicion', blank=True, null=True)  # Field name made lowercase.
    ciudadexpedicion = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='ciudadExpedicion', blank=True, null=True, related_name='AsesoresDb.ciudadexpedicion+')  # Field name made lowercase.
    genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='genero')

    class Meta:
        managed = False
        db_table = 'asesores_db'


class Comisiones(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=20, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comisiones'


class Perfilasesor(models.Model):
    codigo = models.AutoField(primary_key=True)
    perfil = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'perfilasesor'


class Pagador(models.Model):
    codigo = models.AutoField(primary_key=True)
    pagador = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pagador'


class SentenciaConciliacion(models.Model):
    codigo = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'sentencia_conciliacion'


class RegSentencia(models.Model):
    cod = models.AutoField(primary_key=True)
    nosentencia = models.DecimalField(db_column='noSentencia', max_digits=23, decimal_places=0)  # Field name made lowercase.
    actor = models.CharField(max_length=70)
    entidades = models.IntegerField(blank=True, null=True)
    tipo = models.ForeignKey(Pagador, models.DO_NOTHING, db_column='tipo', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    etapa = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    sub_estado = models.IntegerField(blank=True, null=True)
    nodesembolso = models.IntegerField(db_column='noDesembolso', blank=True, null=True)  # Field name made lowercase.
    iddesembolso = models.IntegerField(db_column='iDdesembolso', blank=True, null=True)  # Field name made lowercase.
    codver = models.IntegerField(db_column='codVer', blank=True, null=True)  # Field name made lowercase.
    entidad_condenada = models.CharField(max_length=11)
    tipo_sentencia = models.ForeignKey(SentenciaConciliacion, models.DO_NOTHING, db_column='tipo_sentencia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reg_sentencia'


class PerfilAbogadosentencia(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'perfil_abogadosentencia'


class Abogadosentencia(models.Model):
    codigo = models.AutoField(primary_key=True)
    codreg = models.ForeignKey(RegSentencia, models.DO_NOTHING, db_column='codReg', blank=True, null=True)  # Field name made lowercase.
    abogado = models.ForeignKey(DbAbogados, models.DO_NOTHING, db_column='abogado', blank=True, null=True)
    perfil = models.ForeignKey(PerfilAbogadosentencia, models.DO_NOTHING, db_column='perfil', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abogadosentencia'


class Antecedentesabd(models.Model):
    codigo = models.AutoField(primary_key=True)
    codabogado = models.ForeignKey(DbAbogados, models.DO_NOTHING, db_column='codAbogado')  # Field name made lowercase.
    fecha = models.DateField(blank=True, null=True)
    archivo = models.CharField(max_length=155, blank=True, null=True)
    emitido = models.ForeignKey('JuzgadosTribunales', models.DO_NOTHING, db_column='emitido', blank=True, null=True)
    observacion = models.CharField(max_length=150, blank=True, null=True)
    documento_tipo = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='documento_tipo', blank=True, null=True)
    documento_clase = models.ForeignKey('ClaseDocumento', models.DO_NOTHING, db_column='documento_clase', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antecedentesabd'


class JuzgadosTribunales(models.Model):
    codigo = models.AutoField(primary_key=True)
    jurisdiccion = models.CharField(max_length=255, blank=True, null=True)
    distrito = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='distrito', blank=True, null=True, related_name='JuzgadosTribunales.distrito+')
    circuito = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='circuito', blank=True, null=True, related_name='JuzgadosTribunales.circuito+')
    municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='municipio', blank=True, null=True, related_name='JuzgadosTribunales.municipio+')
    codigo_despacho = models.CharField(max_length=30, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    juez_despacho = models.CharField(max_length=255, blank=True, null=True)
    correo_despacho = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    horario = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='departamento', blank=True, null=True, related_name='JuzgadosTribunales.departamento+')

    class Meta:
        managed = False
        db_table = 'juzgados_tribunales'


class TipoDocumento(models.Model):
    codigo = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class ClaseDocumento(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo_documento = models.ForeignKey(TipoDocumento, models.DO_NOTHING, db_column='tipo_documento', blank=True, null=True)
    documento = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clase_documento'


class OrigenContacto(models.Model):
    codigo = models.AutoField(primary_key=True)
    contacto = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'origen_contacto'
