# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Abogadoscedente(models.Model):
    codigo = models.AutoField(primary_key=True)
    codabogado = models.IntegerField()
    codbeneficiario = models.IntegerField(blank=True, null=True)
    honorarios = models.FloatField(blank=True, null=True)
    cedente = models.IntegerField(blank=True, null=True)
    fallecido = models.IntegerField(blank=True, null=True)
    contrato = models.CharField(max_length=150, blank=True, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abogadoscedente'


class Abogadosentencia(models.Model):
    codigo = models.AutoField(primary_key=True)
    codreg = models.IntegerField(db_column='codReg', blank=True, null=True)  # Field name made lowercase.
    codabogado = models.IntegerField(db_column='codAbogado', blank=True, null=True)  # Field name made lowercase.
    cedente = models.IntegerField(blank=True, null=True)
    honorarios = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abogadosentencia'


class AccesoSentencia(models.Model):
    codigo = models.AutoField(primary_key=True)
    sentencia = models.IntegerField()
    usuario = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'acceso_sentencia'


class Agenda(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    recurrence = models.CharField(max_length=1, blank=True, null=True)
    period = models.CharField(max_length=1, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    id_api = models.CharField(max_length=255, blank=True, null=True)
    id_event_google = models.CharField(max_length=255, blank=True, null=True)
    recur_info = models.CharField(max_length=255, blank=True, null=True)
    event_color = models.CharField(max_length=255, blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    reminder = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.IntegerField(blank=True, null=True)
    terminado = models.IntegerField(blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agenda'


class Antecedentesabd(models.Model):
    codigo = models.AutoField(primary_key=True)
    codabogado = models.IntegerField(db_column='codAbogado')  # Field name made lowercase.
    fecha = models.DateField()
    regrestriccion = models.IntegerField(db_column='regRestriccion', blank=True, null=True)  # Field name made lowercase.
    regarchivo = models.CharField(db_column='regArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    regobservacion = models.CharField(db_column='regObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    proantecedentes = models.IntegerField(db_column='proAntecedentes', blank=True, null=True)  # Field name made lowercase.
    proinicio = models.DateField(db_column='proInicio', blank=True, null=True)  # Field name made lowercase.
    profinal = models.DateField(db_column='proFinal', blank=True, null=True)  # Field name made lowercase.
    prodeuda = models.IntegerField(db_column='proDeuda', blank=True, null=True)  # Field name made lowercase.
    proarchivo = models.CharField(db_column='proArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    proobservacion = models.CharField(db_column='proObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    contantecedentes = models.IntegerField(db_column='contAntecedentes', blank=True, null=True)  # Field name made lowercase.
    contarchivo = models.CharField(db_column='contArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    contobservacion = models.CharField(db_column='contObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    polpendientes = models.IntegerField(db_column='polPendientes', blank=True, null=True)  # Field name made lowercase.
    polarchivo = models.CharField(db_column='polArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    polobservacion = models.CharField(db_column='polObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    diancuenta = models.IntegerField(db_column='dianCuenta', blank=True, null=True)  # Field name made lowercase.
    dianpago = models.CharField(db_column='dianPago', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dianarchivo = models.CharField(db_column='dianArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dianobservacion = models.CharField(db_column='dianObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    csjantecedentes = models.IntegerField(db_column='csjAntecedentes', blank=True, null=True)  # Field name made lowercase.
    csjtp = models.IntegerField(db_column='csjTp', blank=True, null=True)  # Field name made lowercase.
    csjini = models.DateField(db_column='csjIni', blank=True, null=True)  # Field name made lowercase.
    csjfin = models.DateField(db_column='csjFin', blank=True, null=True)  # Field name made lowercase.
    csjarticulo = models.CharField(db_column='csjArticulo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    csjarchivo = models.CharField(db_column='csjArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    csjobservacion = models.CharField(db_column='csjObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sirnavigencia = models.IntegerField(db_column='sirnaVigencia', blank=True, null=True)  # Field name made lowercase.
    sirnarchivo = models.CharField(db_column='sirnArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sirnaobservacion = models.CharField(db_column='sirnaObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cedula = models.IntegerField(blank=True, null=True)
    fechaexpedicion = models.DateField(db_column='fechaExpedicion', blank=True, null=True)  # Field name made lowercase.
    juridico = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antecedentesabd'


class Antecedentesben(models.Model):
    codigo = models.AutoField(primary_key=True)
    codben = models.IntegerField(db_column='codBen')  # Field name made lowercase.
    fecha = models.DateField()
    regrestriccion = models.IntegerField(db_column='regRestriccion', blank=True, null=True)  # Field name made lowercase.
    regarchivo = models.CharField(db_column='regArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    regobservacion = models.CharField(db_column='regObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    proantecedentes = models.IntegerField(db_column='proAntecedentes', blank=True, null=True)  # Field name made lowercase.
    proinicio = models.DateField(db_column='proInicio', blank=True, null=True)  # Field name made lowercase.
    profinal = models.DateField(db_column='proFinal', blank=True, null=True)  # Field name made lowercase.
    prodeuda = models.IntegerField(db_column='proDeuda', blank=True, null=True)  # Field name made lowercase.
    proarchivo = models.CharField(db_column='proArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    proobservacion = models.CharField(db_column='proObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    contantecedentes = models.IntegerField(db_column='contAntecedentes', blank=True, null=True)  # Field name made lowercase.
    contarchivo = models.CharField(db_column='contArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    contobservacion = models.CharField(db_column='contObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    polpendientes = models.IntegerField(db_column='polPendientes', blank=True, null=True)  # Field name made lowercase.
    polarchivo = models.CharField(db_column='polArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    polobservacion = models.CharField(db_column='polObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    listreportado = models.IntegerField(db_column='listReportado', blank=True, null=True)  # Field name made lowercase.
    listarchivo = models.CharField(db_column='listArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    listobservacion = models.CharField(db_column='listObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    diancuenta = models.IntegerField(db_column='dianCuenta', blank=True, null=True)  # Field name made lowercase.
    dianpago = models.CharField(db_column='dianPago', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dianarchivo = models.CharField(db_column='dianArchivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dianobservacion = models.CharField(db_column='dianObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    juridico = models.IntegerField(blank=True, null=True)
    fecha_expedicion = models.DateField(blank=True, null=True)
    cedula = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antecedentesben'


class Apoderado(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    cedula = models.IntegerField(blank=True, null=True)
    ciudadexp = models.IntegerField(db_column='ciudadExp', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=154, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    registro = models.IntegerField(blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    fechaexpedicion = models.DateField(db_column='fechaExpedicion', blank=True, null=True)  # Field name made lowercase.
    genero = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apoderado'


class ArgumentoLibertad(models.Model):
    codigo = models.AutoField(primary_key=True)
    argumento = models.CharField(max_length=20)
    estado = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'argumento_libertad'


class Artregimen(models.Model):
    codigo = models.AutoField(primary_key=True)
    regimen = models.CharField(max_length=5, blank=True, null=True)
    articulo = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artregimen'


class AsesoresDb(models.Model):
    cod_asesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=154, blank=True, null=True)
    ciudad = models.IntegerField(blank=True, null=True)
    direccion2 = models.CharField(max_length=154, blank=True, null=True)
    ciudad2 = models.IntegerField(blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    t_asesor = models.CharField(max_length=15, blank=True, null=True)
    comision = models.IntegerField(blank=True, null=True)
    cedula = models.CharField(max_length=15, blank=True, null=True)
    c_cedula = models.CharField(max_length=150, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fecha_s = models.DateField(blank=True, null=True)
    perfil = models.IntegerField(blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    fechaexpedicion = models.DateField(db_column='fechaExpedicion', blank=True, null=True)  # Field name made lowercase.
    ciudadexpedicion = models.IntegerField(db_column='ciudadExpedicion', blank=True, null=True)  # Field name made lowercase.
    genero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'asesores_db'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Beneficiarios(models.Model):
    codigo = models.AutoField(primary_key=True)
    documentoid = models.IntegerField(db_column='documentoId', blank=True, null=True)  # Field name made lowercase.
    tipoid = models.IntegerField(db_column='tipoId', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    mayor_menor = models.IntegerField(blank=True, null=True)
    consanguinidad = models.IntegerField(blank=True, null=True)
    fallecido = models.IntegerField(blank=True, null=True)
    cedente = models.IntegerField(blank=True, null=True)
    codabogado = models.IntegerField(db_column='codAbogado', blank=True, null=True)  # Field name made lowercase.
    copia_id = models.CharField(max_length=150, blank=True, null=True)
    ciudadexp = models.IntegerField(db_column='ciudadExp', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=150, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=60, blank=True, null=True)
    apoderado = models.IntegerField(blank=True, null=True)
    genero = models.IntegerField()
    fecha_expedicion = models.DateField()
    codreg = models.IntegerField(db_column='codReg', blank=True, null=True)  # Field name made lowercase.
    ciudad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beneficiarios'


class CategoriaCalendario(models.Model):
    codigo = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    departamento = models.IntegerField(blank=True, null=True)
    dias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria_calendario'


class CcaCpaca(models.Model):
    codigo = models.AutoField(primary_key=True)
    regimen = models.CharField(max_length=6)
    fecha = models.DateField()
    interes = models.FloatField()
    plazo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cca_cpaca'


class CheckList(models.Model):
    codigo = models.AutoField(primary_key=True)
    codreg = models.IntegerField(db_column='codReg', unique=True, blank=True, null=True)  # Field name made lowercase.
    cuentacobro = models.IntegerField(db_column='cuentaCobro', blank=True, null=True)  # Field name made lowercase.
    ejecutoria = models.IntegerField(blank=True, null=True)
    pcopias = models.IntegerField(db_column='pCopias', blank=True, null=True)  # Field name made lowercase.
    vpoderes = models.IntegerField(db_column='vPoderes', blank=True, null=True)  # Field name made lowercase.
    piniciales = models.IntegerField(db_column='pIniciales', blank=True, null=True)  # Field name made lowercase.
    rpoder = models.IntegerField(db_column='rPoder', blank=True, null=True)  # Field name made lowercase.
    suspoderes = models.IntegerField(db_column='susPoderes', blank=True, null=True)  # Field name made lowercase.
    primerainstancia = models.IntegerField(db_column='primeraInstancia', blank=True, null=True)  # Field name made lowercase.
    segundainstancia = models.IntegerField(db_column='segundaInstancia', blank=True, null=True)  # Field name made lowercase.
    sucesion = models.IntegerField(blank=True, null=True)
    conciliacion = models.IntegerField(blank=True, null=True)
    autoaprueba = models.IntegerField(db_column='autoAprueba', blank=True, null=True)  # Field name made lowercase.
    automodifica = models.IntegerField(db_column='autoModifica', blank=True, null=True)  # Field name made lowercase.
    autoconfirma = models.IntegerField(db_column='autoConfirma', blank=True, null=True)  # Field name made lowercase.
    autoaclara = models.IntegerField(db_column='autoAclara', blank=True, null=True)  # Field name made lowercase.
    revisionjuridica = models.IntegerField(db_column='revisionJuridica', blank=True, null=True)  # Field name made lowercase.
    poderrecibir = models.IntegerField(db_column='poderRecibir', blank=True, null=True)  # Field name made lowercase.
    visitainsitu = models.IntegerField(db_column='visitaInsitu', blank=True, null=True)  # Field name made lowercase.
    alcancecesion = models.IntegerField(db_column='alcanceCesion', blank=True, null=True)  # Field name made lowercase.
    turnopago = models.IntegerField(db_column='turnoPago', blank=True, null=True)  # Field name made lowercase.
    instrucciongiro = models.IntegerField(db_column='instruccionGiro', blank=True, null=True)  # Field name made lowercase.
    certificacionbco = models.IntegerField(db_column='certificacionBco', blank=True, null=True)  # Field name made lowercase.
    liquidacion = models.IntegerField(blank=True, null=True)
    otorgamientopoder = models.IntegerField(db_column='otorgamientoPoder', blank=True, null=True)  # Field name made lowercase.
    poderrevisar = models.IntegerField(db_column='poderRevisar', blank=True, null=True)  # Field name made lowercase.
    poderdian = models.IntegerField(db_column='poderDian', blank=True, null=True)  # Field name made lowercase.
    podercesion = models.IntegerField(db_column='poderCesion', blank=True, null=True)  # Field name made lowercase.
    acuerdocontrato = models.IntegerField(db_column='acuerdoContrato', blank=True, null=True)  # Field name made lowercase.
    pyshonorarios = models.IntegerField(db_column='pysHonorarios', blank=True, null=True)  # Field name made lowercase.
    pyscontrato = models.IntegerField(db_column='pysContrato', blank=True, null=True)  # Field name made lowercase.
    pyscadena = models.IntegerField(db_column='pysCadena', blank=True, null=True)  # Field name made lowercase.
    cesionnot = models.IntegerField(db_column='cesionNot', blank=True, null=True)  # Field name made lowercase.
    desarchive = models.IntegerField(blank=True, null=True)
    cesioncadena = models.IntegerField(db_column='cesionCadena', blank=True, null=True)  # Field name made lowercase.
    regarchivo_abd = models.IntegerField(db_column='regArchivo_Abd', blank=True, null=True)  # Field name made lowercase.
    proarchivo_abd = models.IntegerField(db_column='proArchivo_Abd', blank=True, null=True)  # Field name made lowercase.
    polarchivo_abd = models.IntegerField(db_column='polArchivo_Abd', blank=True, null=True)  # Field name made lowercase.
    listarchivo_abd = models.IntegerField(db_column='listArchivo_Abd', blank=True, null=True)  # Field name made lowercase.
    dianarchivo_abd = models.IntegerField(db_column='dianArchivo_Abd', blank=True, null=True)  # Field name made lowercase.
    csjarchivo_abd = models.IntegerField(db_column='csjArchivo_Abd', blank=True, null=True)  # Field name made lowercase.
    sirnaarchivo_abd = models.IntegerField(db_column='sirnaArchivo_Abd', blank=True, null=True)  # Field name made lowercase.
    regarchivo_ben = models.IntegerField(db_column='regArchivo_ben', blank=True, null=True)  # Field name made lowercase.
    proarchivo_ben = models.IntegerField(db_column='proArchivo_ben', blank=True, null=True)  # Field name made lowercase.
    contarchivo_ben = models.IntegerField(db_column='contArchivo_ben', blank=True, null=True)  # Field name made lowercase.
    polarchivo_ben = models.IntegerField(db_column='polArchivo_ben', blank=True, null=True)  # Field name made lowercase.
    listarchivo_ben = models.IntegerField(db_column='listArchivo_ben', blank=True, null=True)  # Field name made lowercase.
    dianarchivo_ben = models.IntegerField(db_column='dianArchivo_ben', blank=True, null=True)  # Field name made lowercase.
    copiacc_abd = models.IntegerField(db_column='copiaCc_abd', blank=True, null=True)  # Field name made lowercase.
    copiatp_abd = models.IntegerField(db_column='copiaTp_abd', blank=True, null=True)  # Field name made lowercase.
    copiaid_ben = models.IntegerField(db_column='copiaId_ben', blank=True, null=True)  # Field name made lowercase.
    cobroobservacion = models.CharField(db_column='cobroObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    ejecutoriaobservacion = models.CharField(db_column='ejecutoriaObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    pcopiasobservacion = models.CharField(db_column='pcopiasObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    vpoderesobservacion = models.CharField(db_column='vPoderesObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    pinicialesobservacion = models.CharField(db_column='pInicialesObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    rpoderobservacion = models.CharField(db_column='rPoderObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    suspoderesobservacion = models.CharField(db_column='susPoderesObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    primeraobservacion = models.CharField(db_column='primeraObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    segundaobservacion = models.CharField(db_column='segundaObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    sucesionobservacion = models.CharField(db_column='sucesionObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    conciliacionobservacion = models.CharField(db_column='conciliacionObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    probatorioobservacion = models.CharField(db_column='probatorioObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    modificaobservacion = models.CharField(db_column='modificaObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    confirmaobservacion = models.CharField(db_column='confirmaObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    aclaraobservacion = models.CharField(db_column='aclaraObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    poderrecibirobservacion = models.CharField(db_column='poderRecibirObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    revisarobservacion = models.CharField(db_column='revisarObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    poddianobservacion = models.CharField(db_column='podDianObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    podcesionobservacion = models.CharField(db_column='podCesionObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    acuerdoctoobservacion = models.CharField(db_column='acuerdoCtoObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    honorariospysobservacion = models.CharField(db_column='honorariosPysObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    contratopysobservacion = models.CharField(db_column='contratoPysObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    cesionctoobservacion = models.CharField(db_column='cesionCtoObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    cadenapysobservacion = models.CharField(db_column='cadenaPysObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    cesionnotobservacion = models.CharField(db_column='cesionNotObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    desarchiveibservacion = models.CharField(db_column='desarchiveIbservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    cesioncadenaobservacion = models.CharField(db_column='cesionCadenaObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    visitaobservacion = models.CharField(db_column='visitaObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    alcanceobservacion = models.CharField(db_column='alcanceObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    turnoobservacion = models.CharField(db_column='turnoObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    instruccionobservacion = models.CharField(db_column='instruccionObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    certificacionbcoobservacion = models.CharField(db_column='certificacionBcoObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    liquidacionobservacion = models.CharField(db_column='liquidacionObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    otorgamientoobservacion = models.CharField(db_column='otorgamientoObservacion', max_length=155, blank=True, null=True)  # Field name made lowercase.
    ctocesion = models.IntegerField(db_column='ctoCesion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'check_list'


class Ciiu(models.Model):
    codigo = models.AutoField(primary_key=True)
    seccion = models.CharField(max_length=50, blank=True, null=True)
    division = models.CharField(max_length=50, blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)
    clase = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciiu'


class Comisiones(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=20, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comisiones'


class Comunicaciones(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    archivo = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comunicaciones'


class ConfivalDepartamentos(models.Model):
    codigo = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=25)
    grupo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confival_departamentos'


class Consanguinidad(models.Model):
    codigo = models.AutoField(primary_key=True)
    beneficiario = models.CharField(max_length=25)
    nivel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consanguinidad'


class ConstanciaSecretarial(models.Model):
    codigo = models.AutoField(primary_key=True)
    fechaejecutoria = models.DateField(db_column='fechaEjecutoria', blank=True, null=True)  # Field name made lowercase.
    fecha_conssecretarial = models.DateField(db_column='fecha_consSecretarial', blank=True, null=True)  # Field name made lowercase.
    vigenciapoderes = models.IntegerField(db_column='vigenciaPoderes', blank=True, null=True)  # Field name made lowercase.
    emitido = models.IntegerField(blank=True, null=True)
    primerascopias = models.IntegerField(db_column='primerasCopias', blank=True, null=True)  # Field name made lowercase.
    codreg = models.IntegerField(db_column='codReg')  # Field name made lowercase.
    observaciones = models.TextField(blank=True, null=True)
    juridico = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'constancia_secretarial'


class Conyugue(models.Model):
    codigo = models.AutoField(primary_key=True)
    codben = models.IntegerField(db_column='codBen')  # Field name made lowercase.
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    tipo_identificacion = models.IntegerField()
    identificacion = models.IntegerField()
    direccion = models.CharField(max_length=155)
    telefono = models.IntegerField()
    celular = models.IntegerField()
    tipo_ocupacion = models.IntegerField()
    empresa_actividad = models.IntegerField()
    genero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conyugue'


class Dano(models.Model):
    codigo = models.AutoField(primary_key=True)
    dano = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'dano'


class DbAbogados(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=51)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    cedula = models.IntegerField(blank=True, null=True)
    tarjeta_p = models.IntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=154, blank=True, null=True)
    ciudad = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='ciudad', blank=True, null=True, related_name='ciudad')
    ciudadnombre = models.CharField(db_column='ciudadNombre', max_length=27, blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(max_length=18, blank=True, null=True)
    direccion2 = models.CharField(max_length=154, blank=True, null=True)
    ciudad2 = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='ciudad2', blank=True, null=True, related_name='ciudad2')
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
    contacto = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateField(blank=True, null=True)
    actualizacion = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)
    copiacc = models.CharField(db_column='copiaCc', max_length=150, blank=True, null=True)  # Field name made lowercase.
    copiatp = models.CharField(db_column='copiaTp', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechaexpedicion = models.DateField(db_column='fechaExpedicion', blank=True, null=True)  # Field name made lowercase.
    ciudadexpedicion = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='ciudadExpedicion', blank=True, null=True, related_name='ciudadexpedicion')  # Field name made lowercase.
    genero = models.ForeignKey('Genero', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_abogados'


class Desembolso(models.Model):
    codigo = models.AutoField(primary_key=True)
    codreg = models.IntegerField(db_column='codReg')  # Field name made lowercase.
    visitainstitu = models.DateField(db_column='visitaInstitu', blank=True, null=True)  # Field name made lowercase.
    visitanombre = models.CharField(db_column='visitaNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    visitaemitido = models.CharField(db_column='visitaEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    visitaobservacion = models.CharField(db_column='visitaObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    alcancecesion = models.DateField(db_column='alcanceCesion', blank=True, null=True)  # Field name made lowercase.
    alcancecesionnombre = models.CharField(db_column='alcanceCesionNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    alcancecesionemitido = models.CharField(db_column='alcanceCesionEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alcancecesionobservacion = models.CharField(db_column='alcanceCesionObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    aceptacioncesion = models.DateField(db_column='aceptacionCesion', blank=True, null=True)  # Field name made lowercase.
    acept_cesionnombre = models.CharField(db_column='acept_cesionNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    acept_cesionemitido = models.CharField(db_column='acept_cesionEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acept_cesionobservacion = models.CharField(db_column='acept_cesionObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    turnopago = models.DateField(db_column='turnoPago', blank=True, null=True)  # Field name made lowercase.
    noturno = models.CharField(db_column='noTurno', max_length=30, blank=True, null=True)  # Field name made lowercase.
    turnoarchivonombre = models.CharField(db_column='turnoArchivoNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    turnoarchivoemitido = models.CharField(db_column='turnoArchivoEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    turnoarchivoobservacion = models.CharField(db_column='turnoArchivoObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    instruccion = models.DateField(blank=True, null=True)
    instrucgironombre = models.CharField(db_column='instrucGiroNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    instrucgiroemitido = models.CharField(db_column='instrucGiroEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    instrucgiroobservacion = models.CharField(db_column='instrucGiroObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    certificacionbco = models.DateField(db_column='certificacionBco', blank=True, null=True)  # Field name made lowercase.
    bcocertificacionnombre = models.CharField(db_column='bcoCertificacionNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bcocertificacionemitido = models.CharField(db_column='bcoCertificacionEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bcocertificacionobservacion = models.CharField(db_column='bcoCertificacionObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    liquidacionfin = models.DateField(db_column='liquidacionFin', blank=True, null=True)  # Field name made lowercase.
    liquidacionnombre = models.CharField(db_column='liquidacionNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    liquidacionemitido = models.CharField(db_column='liquidacionEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    liquidacionobservacion = models.CharField(db_column='liquidacionObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechaotorgamiento = models.DateField(db_column='fechaOtorgamiento', blank=True, null=True)  # Field name made lowercase.
    otorgamientopodernombre = models.CharField(db_column='otorgamientoPoderNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    otorgamientopoderemitido = models.CharField(db_column='otorgamientoPoderEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otorgamientopoderobservacion = models.CharField(db_column='otorgamientoPoderObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'desembolso'


class Desicion(models.Model):
    codigo = models.AutoField(primary_key=True)
    desicion = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'desicion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documentoscesion(models.Model):
    codigo = models.AutoField(primary_key=True)
    codreg = models.IntegerField(db_column='codReg')  # Field name made lowercase.
    podrevisar = models.DateField(db_column='podRevisar', blank=True, null=True)  # Field name made lowercase.
    revisarnombre = models.CharField(db_column='revisarNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    revisaremitido = models.CharField(db_column='revisarEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    revisarobservacion = models.CharField(db_column='revisarObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    poderdian = models.DateField(db_column='poderDian', blank=True, null=True)  # Field name made lowercase.
    poddiannombre = models.CharField(db_column='podDianNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    poddianemitido = models.CharField(db_column='podDianEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poddianobservacion = models.CharField(db_column='podDianObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    podercesion = models.DateField(db_column='poderCesion', blank=True, null=True)  # Field name made lowercase.
    podcesionnombre = models.CharField(db_column='podCesionNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    podcesionemitido = models.CharField(db_column='podCesionEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    podcesionobservacion = models.CharField(db_column='podCesionObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ctoacuerdo = models.DateField(db_column='ctoAcuerdo', blank=True, null=True)  # Field name made lowercase.
    acuerdoctonombre = models.CharField(db_column='acuerdoCtoNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    acuerdoctoemitido = models.CharField(db_column='acuerdoCtoEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acuerdoctoobservacion = models.CharField(db_column='acuerdoCtoObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    pyshonorarios = models.DateField(db_column='pysHonorarios', blank=True, null=True)  # Field name made lowercase.
    honorariospysnombre = models.CharField(db_column='honorariosPysNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    honorariospysemitido = models.CharField(db_column='honorariosPysEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    honorariospysobservacion = models.CharField(db_column='honorariosPysObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    pyscontrato = models.DateField(db_column='pysContrato', blank=True, null=True)  # Field name made lowercase.
    contratopysnombre = models.CharField(db_column='contratoPysNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    contratopysemitido = models.CharField(db_column='contratoPysEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contratopysobservacion = models.CharField(db_column='contratoPysObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ctocesion = models.DateField(db_column='ctoCesion', blank=True, null=True)  # Field name made lowercase.
    cesionctonombre = models.CharField(db_column='cesionCtoNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cesionctoemitido = models.CharField(db_column='cesionCtoEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cesionctoobservacion = models.CharField(db_column='cesionCtoObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    pyscadena = models.DateField(db_column='pysCadena', blank=True, null=True)  # Field name made lowercase.
    cadenapysnombre = models.CharField(db_column='cadenaPysNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cadenapysemitido = models.CharField(db_column='cadenaPysEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cadenapysobservacion = models.CharField(db_column='cadenaPysObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    notcesion = models.DateField(db_column='notCesion', blank=True, null=True)  # Field name made lowercase.
    cesionnotnombre = models.CharField(db_column='cesionNotNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cesionnotemitido = models.CharField(db_column='cesionNotEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cesionnotobservacion = models.CharField(db_column='cesionNotObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    desarchive = models.DateField(blank=True, null=True)
    desarchivenombre = models.CharField(db_column='desarchiveNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    desarchiveemitido = models.CharField(db_column='desarchiveEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    desarchiveibservacion = models.CharField(db_column='desarchiveIbservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechacesioncadena = models.DateField(db_column='fechaCesionCadena', blank=True, null=True)  # Field name made lowercase.
    cesioncadenanombre = models.CharField(db_column='cesionCadenaNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cesioncadenaemitido = models.CharField(db_column='cesionCadenaEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cesioncadenaobservacion = models.CharField(db_column='cesionCadenaObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'documentoscesion'


class Dtf90(models.Model):
    codigo = models.AutoField(primary_key=True)
    anomes = models.DateField(db_column='a±oMes', blank=True, null=True)  # Field name made lowercase.
    cdt90 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dtf90'


class Entidad(models.Model):
    codigo = models.AutoField(primary_key=True)
    entidad = models.CharField(max_length=255, blank=True, null=True)
    nit_entidad = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entidad'


class Entidadcondenada(models.Model):
    codigo = models.AutoField(primary_key=True)
    entidadcondenada = models.IntegerField(db_column='entidadCondenada', blank=True, null=True)  # Field name made lowercase.
    fallo = models.IntegerField(blank=True, null=True)
    tipofallo = models.IntegerField(db_column='tipoFallo', blank=True, null=True)  # Field name made lowercase.
    fechacuenta = models.DateField(db_column='fechaCuenta', blank=True, null=True)  # Field name made lowercase.
    fechaturno = models.DateField(db_column='fechaTurno', blank=True, null=True)  # Field name made lowercase.
    fechaasignacion = models.DateField(db_column='fechaAsignacion', blank=True, null=True)  # Field name made lowercase.
    fecharequisitos = models.DateField(db_column='fechaRequisitos', blank=True, null=True)  # Field name made lowercase.
    noturno = models.CharField(db_column='noTurno', max_length=40, blank=True, null=True)  # Field name made lowercase.
    actor = models.CharField(max_length=70, blank=True, null=True)
    entidades = models.IntegerField(blank=True, null=True)
    declaracion = models.IntegerField(blank=True, null=True)
    comentariosdeclara = models.CharField(max_length=70, blank=True, null=True)
    copiaben = models.IntegerField(db_column='copiaBen', blank=True, null=True)  # Field name made lowercase.
    comentariocopiaben = models.CharField(db_column='comentariocopiaBen', max_length=70, blank=True, null=True)  # Field name made lowercase.
    copiaapo = models.IntegerField(db_column='copiaApo', blank=True, null=True)  # Field name made lowercase.
    comentariocopiaapo = models.CharField(db_column='comentarioCopiaApo', max_length=70, blank=True, null=True)  # Field name made lowercase.
    fjudiciales = models.IntegerField(db_column='fJudiciales', blank=True, null=True)  # Field name made lowercase.
    comentariofjudiciales = models.CharField(db_column='comentariofJudiciales', max_length=70, blank=True, null=True)  # Field name made lowercase.
    pricopias = models.IntegerField(db_column='priCopias', blank=True, null=True)  # Field name made lowercase.
    comentariospricopias = models.CharField(db_column='comentariospriCopias', max_length=70, blank=True, null=True)  # Field name made lowercase.
    fechaejecutoria = models.IntegerField(blank=True, null=True)
    comentariofechaejecutoria = models.CharField(max_length=70, blank=True, null=True)
    vigpoderes = models.IntegerField(db_column='vigPoderes', blank=True, null=True)  # Field name made lowercase.
    comentariovigpoderes = models.CharField(db_column='comentariovigPoderes', max_length=70, blank=True, null=True)  # Field name made lowercase.
    poderes = models.IntegerField(blank=True, null=True)
    comentariopoderes = models.CharField(db_column='comentarioPoderes', max_length=70, blank=True, null=True)  # Field name made lowercase.
    demas_documentos = models.IntegerField(blank=True, null=True)
    comentario_documentos = models.CharField(max_length=70, blank=True, null=True)
    cerbancaria = models.IntegerField(blank=True, null=True)
    comentariocerbancaria = models.CharField(max_length=70, blank=True, null=True)
    idbeneficiarios = models.IntegerField(db_column='idBeneficiarios', blank=True, null=True)  # Field name made lowercase.
    comentarioidbeneficiarios = models.CharField(db_column='comentarioidBeneficiarios', max_length=70, blank=True, null=True)  # Field name made lowercase.
    idapoderado = models.IntegerField(db_column='idApoderado', blank=True, null=True)  # Field name made lowercase.
    comentarioidapoderado = models.CharField(db_column='comentarioidApoderado', max_length=70, blank=True, null=True)  # Field name made lowercase.
    rutben = models.IntegerField(db_column='rutBen', blank=True, null=True)  # Field name made lowercase.
    comentariorutben = models.CharField(db_column='comentariorutBen', max_length=70, blank=True, null=True)  # Field name made lowercase.
    rutapoderado = models.IntegerField(db_column='rutApoderado', blank=True, null=True)  # Field name made lowercase.
    comentariorutapoderado = models.CharField(db_column='comentariorutApoderado', max_length=70, blank=True, null=True)  # Field name made lowercase.
    comercial = models.IntegerField(blank=True, null=True)
    hechos = models.TextField(blank=True, null=True)
    regimen_intereses = models.IntegerField(blank=True, null=True)
    articulo_intereses = models.CharField(max_length=15, blank=True, null=True)
    monto = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    monto_slm = models.IntegerField(blank=True, null=True)
    apoderado = models.IntegerField(db_column='Apoderado', blank=True, null=True)  # Field name made lowercase.
    contacto_cliente = models.IntegerField(blank=True, null=True)
    documento = models.IntegerField(blank=True, null=True)
    referenciado_por = models.IntegerField(blank=True, null=True)
    comision_externa = models.IntegerField(blank=True, null=True)
    regimen_imputacion = models.IntegerField(blank=True, null=True)
    titulo_imputacion = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)
    nivel_dano = models.IntegerField(blank=True, null=True)
    fecha_ejecutoria = models.DateField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entidadcondenada'


class EstadoCivil(models.Model):
    codigo = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'estado_civil'


class Estadodocumentos(models.Model):
    codigo = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estadodocumentos'


class Estadooperacion(models.Model):
    codigo = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estadooperacion'


class Estados(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha_val = models.DateField()
    tasa_p = models.FloatField()
    rendimientos_val = models.DecimalField(max_digits=15, decimal_places=2)
    nit_f = models.CharField(max_length=255)
    operacion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'estados'


class FechaFestivos(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    vn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fecha_festivos'


class Genero(models.Model):
    codigo = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'genero'


class Iddesembolso(models.Model):
    codigo = models.AutoField(primary_key=True)
    id = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'iddesembolso'


class Imputacion(models.Model):
    codigo = models.AutoField(primary_key=True)
    imputacion = models.CharField(max_length=60)
    regimen = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'imputacion'


class Inversores(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=60, blank=True, null=True)
    apellidos = models.CharField(max_length=60, blank=True, null=True)
    nit_cc = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=155, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=60, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    empresa = models.CharField(max_length=60, blank=True, null=True)
    ciudad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inversores'


class Ipc(models.Model):
    codigo = models.AutoField(primary_key=True)
    ano_mes = models.CharField(max_length=20)
    ipc = models.FloatField()
    var_mensual = models.FloatField()
    var_anocorrido = models.FloatField(db_column='var_a±oCorrido')  # Field name made lowercase.
    var_anual = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ipc'


class Juridicos(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=154)
    ciudad = models.IntegerField()
    mail = models.CharField(max_length=50)
    fijo = models.CharField(max_length=15)
    cedula = models.CharField(max_length=15)
    fecha = models.DateField()
    tarjetaprofesional = models.CharField(db_column='tarjetaProfesional', max_length=30)  # Field name made lowercase.
    fecha_s = models.DateField()
    perfil = models.IntegerField()
    genero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'juridicos'


class JuzgadosTribunales(models.Model):
    codigo = models.AutoField(primary_key=True)
    jurisdiccion = models.CharField(max_length=255, blank=True, null=True)
    distrito = models.CharField(max_length=255, blank=True, null=True)
    circuito = models.CharField(max_length=255, blank=True, null=True)
    municipio = models.CharField(max_length=255, blank=True, null=True)
    codigo_despacho = models.CharField(max_length=30, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    juez_despacho = models.CharField(max_length=255, blank=True, null=True)
    correo_despacho = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    horario = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'juzgados_tribunales'


class ListaCsj(models.Model):
    codigo = models.AutoField(primary_key=True)
    sancion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'lista_csj'


class ListaDian(models.Model):
    codigo = models.AutoField(primary_key=True)
    consulta = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'lista_dian'


class ListaProcuraduria(models.Model):
    codigo = models.AutoField(primary_key=True)
    sancion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'lista_procuraduria'


class ListaRegistraduria(models.Model):
    codigo = models.AutoField(primary_key=True)
    consulta = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'lista_registraduria'


class Listadeclaracion(models.Model):
    codigo = models.AutoField(primary_key=True)
    declaracion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'listadeclaracion'


class MayorMenor(models.Model):
    codigo = models.AutoField(primary_key=True)
    mayor_menor = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mayor_menor'


class Motivorechazo(models.Model):
    codigo = models.AutoField(primary_key=True)
    rechazo = models.CharField(max_length=50)
    condicion = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'motivorechazo'


class Municipio(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_dane = models.CharField(max_length=15)
    departamento = models.CharField(max_length=18)
    municipio = models.CharField(max_length=27)

    class Meta:
        managed = False
        db_table = 'municipio'


class NivelAcademico(models.Model):
    codigo = models.AutoField(primary_key=True)
    nivel = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'nivel_academico'


class Ocupacion(models.Model):
    codigo = models.AutoField(primary_key=True)
    ocupacion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'ocupacion'


class Operaciones(models.Model):
    codigo = models.AutoField(primary_key=True)
    operacion = models.CharField(max_length=255)
    fechaoperacion = models.DateField()
    sentencia = models.CharField(max_length=255)
    cc_actor = models.IntegerField()
    nit_pagaduria = models.IntegerField()
    val_sentencia = models.DecimalField(max_digits=15, decimal_places=2)
    facial = models.DecimalField(max_digits=15, decimal_places=2)
    val_adquirido = models.DecimalField(max_digits=15, decimal_places=2)
    por_adquirido = models.FloatField()
    nit_f = models.IntegerField()
    estado = models.IntegerField()
    observacion = models.CharField(max_length=150)
    tasa_pactada = models.FloatField()
    fecha_ingreso = models.DateField()
    minv_pre = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_cierre = models.DateField()
    saldo_fcierre = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_estimadapago = models.DateField()
    tiempo_estimado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'operaciones'


class OrigenContacto(models.Model):
    codigo = models.AutoField(primary_key=True)
    contacto = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'origen_contacto'


class Pagador(models.Model):
    codigo = models.AutoField(primary_key=True)
    pagador = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pagador'


class Pasosnegociacion(models.Model):
    codigo = models.AutoField(primary_key=True)
    etapa = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pasosnegociacion'


class Perfil(models.Model):
    codigo = models.AutoField(primary_key=True)
    perfil = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'perfil'


class PerfilApoderado(models.Model):
    codigo = models.AutoField(primary_key=True)
    perfil = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'perfil_apoderado'


class Perfilasesor(models.Model):
    codigo = models.AutoField(primary_key=True)
    perfil = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'perfilasesor'


class Perfiljuridico(models.Model):
    codigo = models.AutoField(primary_key=True)
    perfil = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'perfiljuridico'


class Referencias(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo_referencia = models.IntegerField()
    codben = models.IntegerField(db_column='codBen')  # Field name made lowercase.
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    parentesco = models.CharField(max_length=50)
    celular = models.IntegerField()
    telefono = models.IntegerField()
    ciudad = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'referencias'


class RegSentencia(models.Model):
    cod = models.AutoField(primary_key=True)
    nosentencia = models.DecimalField(db_column='noSentencia', max_digits=23, decimal_places=0)  # Field name made lowercase.
    actor = models.CharField(max_length=70)
    entidades = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    etapa = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    sub_estado = models.IntegerField(blank=True, null=True)
    nodesembolso = models.IntegerField(db_column='noDesembolso', blank=True, null=True)  # Field name made lowercase.
    iddesembolso = models.IntegerField(db_column='iDdesembolso', blank=True, null=True)  # Field name made lowercase.
    codver = models.IntegerField(db_column='codVer', blank=True, null=True)  # Field name made lowercase.
    entidad_condenada = models.IntegerField()
    tipo_sentencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reg_sentencia'


class RegimenImputacion(models.Model):
    codigo = models.AutoField(primary_key=True)
    regimen = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'regimen_imputacion'


class Relacionapoderado(models.Model):
    codigo = models.AutoField(primary_key=True)
    actor = models.CharField(max_length=150, blank=True, null=True)
    beneficiario = models.IntegerField(blank=True, null=True)
    codabd = models.IntegerField(db_column='codAbd', blank=True, null=True)  # Field name made lowercase.
    codapo = models.IntegerField(db_column='codApo', blank=True, null=True)  # Field name made lowercase.
    codben = models.IntegerField(db_column='codBen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relacionapoderado'


class RepDocdemandantes(models.Model):
    codigo = models.AutoField(primary_key=True)
    codben = models.IntegerField(db_column='codBen')  # Field name made lowercase.
    copia_id = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'rep_docdemandantes'


class RepSentencia(models.Model):
    codigo = models.AutoField(primary_key=True)
    codreg = models.IntegerField(db_column='codReg')  # Field name made lowercase.
    fechacuenta = models.DateField(db_column='fechaCuenta', blank=True, null=True)  # Field name made lowercase.
    ctaentidad = models.IntegerField(db_column='Ctaentidad', blank=True, null=True)  # Field name made lowercase.
    ctadeclaracion = models.IntegerField(db_column='Ctadeclaracion', blank=True, null=True)  # Field name made lowercase.
    cobronombre = models.CharField(db_column='cobroNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cobroemitido = models.CharField(db_column='cobroEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cobroobservacion = models.CharField(db_column='cobroObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechaejecutoria = models.DateField(db_column='fechaEjecutoria', blank=True, null=True)  # Field name made lowercase.
    ejecutorianombre = models.CharField(db_column='ejecutoriaNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ejecutoriaemitida = models.CharField(db_column='ejecutoriaEmitida', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ejecutoriaobservacion = models.CharField(db_column='ejecutoriaObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechapcopias = models.DateField(blank=True, null=True)
    pcopiasnombre = models.CharField(db_column='pcopiasNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    pcopiasemitido = models.CharField(db_column='pcopiasEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pcopiasobservacion = models.CharField(db_column='pcopiasObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechavpoderes = models.DateField(db_column='fechavPoderes', blank=True, null=True)  # Field name made lowercase.
    vpoderesnombre = models.CharField(db_column='vPoderesNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    vpoderesemitido = models.CharField(db_column='vPoderesEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vpoderesobservacion = models.CharField(db_column='vPoderesObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechapiniciales = models.DateField(db_column='fechapIniciales', blank=True, null=True)  # Field name made lowercase.
    pinicialesnombre = models.CharField(db_column='pInicialesNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    pinicialesemitido = models.CharField(db_column='pInicialesEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pinicialesobservacion = models.CharField(db_column='pInicialesObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fecharpoder = models.DateField(db_column='fecharPoder', blank=True, null=True)  # Field name made lowercase.
    rpodernombre = models.CharField(db_column='rPoderNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    rpoderemitido = models.CharField(db_column='rPoderEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rpoderobservacion = models.CharField(db_column='rPoderObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechasuspoderes = models.DateField(db_column='fechasusPoderes', blank=True, null=True)  # Field name made lowercase.
    suspoderesnombre = models.CharField(db_column='susPoderesNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    suspoderesemitido = models.CharField(db_column='susPoderesEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suspoderesobservacion = models.CharField(db_column='susPoderesObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechaprimera = models.DateField(db_column='fechaPrimera', blank=True, null=True)  # Field name made lowercase.
    primeranombre = models.CharField(db_column='primeraNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    primeraemitida = models.CharField(db_column='primeraEmitida', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primeraobservacion = models.CharField(db_column='primeraObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechasegunda = models.DateField(db_column='fechaSegunda', blank=True, null=True)  # Field name made lowercase.
    segundanombre = models.CharField(db_column='segundaNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    segundaemitida = models.CharField(db_column='segundaEmitida', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundaobservacion = models.CharField(db_column='segundaObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechasucesion = models.DateField(db_column='fechaSucesion', blank=True, null=True)  # Field name made lowercase.
    sucesionnombre = models.CharField(db_column='sucesionNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sucesionemitido = models.CharField(db_column='sucesionEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sucesionobservacion = models.CharField(db_column='sucesionObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechaconciliacion = models.DateField(db_column='fechaConciliacion', blank=True, null=True)  # Field name made lowercase.
    conciliacionnombre = models.CharField(db_column='conciliacionNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    conciliacionemitida = models.CharField(db_column='conciliacionEmitida', max_length=50, blank=True, null=True)  # Field name made lowercase.
    conciliacionobservacion = models.CharField(db_column='conciliacionObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechaprobatorio = models.DateField(db_column='fechaProbatorio', blank=True, null=True)  # Field name made lowercase.
    probatorionombre = models.CharField(db_column='probatorioNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    probatorioemitido = models.CharField(db_column='probatorioEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    probatorioobservacion = models.CharField(db_column='probatorioObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechamodifica = models.DateField(db_column='fechaModifica', blank=True, null=True)  # Field name made lowercase.
    modificanombre = models.CharField(db_column='modificaNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    modificaemitido = models.CharField(db_column='modificaEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modificaobservacion = models.CharField(db_column='modificaObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechaconfirma = models.DateField(db_column='fechaConfirma', blank=True, null=True)  # Field name made lowercase.
    confirmanombre = models.CharField(db_column='confirmaNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    confirmaemitido = models.CharField(db_column='confirmaEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirmaobservacion = models.CharField(db_column='confirmaObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechaaclara = models.DateField(db_column='fechaAclara', blank=True, null=True)  # Field name made lowercase.
    aclaranombre = models.CharField(db_column='aclaraNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    aclaraemitido = models.CharField(db_column='aclaraEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    aclaraobservacion = models.CharField(db_column='aclaraObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechajuridica = models.DateField(db_column='fechaJuridica', blank=True, null=True)  # Field name made lowercase.
    revisionjuridicanombre = models.CharField(db_column='revisionJuridicaNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    juridico = models.IntegerField(blank=True, null=True)
    fechapoderrecibir = models.DateField(db_column='fechaPoderRecibir', blank=True, null=True)  # Field name made lowercase.
    poderrecibirnombre = models.CharField(db_column='poderRecibirNombre', max_length=150, blank=True, null=True)  # Field name made lowercase.
    poderrecibiremitido = models.CharField(db_column='poderRecibirEmitido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    poderrecibirobservacion = models.CharField(db_column='poderRecibirObservacion', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rep_sentencia'


class Resumenestado(models.Model):
    codigo = models.AutoField(primary_key=True)
    dias_inv = models.CharField(max_length=25)
    fecha_corte = models.DateField()
    total_parpreferente = models.DecimalField(max_digits=15, decimal_places=0)
    derechos_preferente = models.DecimalField(max_digits=15, decimal_places=0)
    operacion = models.CharField(max_length=255)
    nit_f = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'resumenestado'


class Salariomin(models.Model):
    codigo = models.AutoField(primary_key=True)
    ano = models.TextField()  # This field type is a guess.
    slm = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salariomin'


class Saldos(models.Model):
    cod = models.AutoField(primary_key=True)
    fecha_saldo = models.DateField()
    operacion = models.CharField(max_length=255)
    saldo = models.DecimalField(max_digits=15, decimal_places=2)
    tasa_p = models.FloatField()
    nit_f = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'saldos'


class ScLog(models.Model):
    id = models.IntegerField()
    inserted_date = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=90)
    application = models.CharField(max_length=200)
    creator = models.CharField(max_length=30)
    ip_user = models.CharField(max_length=32)
    action = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_log'


class Seguimiento(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre_apellido = models.IntegerField(blank=True, null=True)
    actividad = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    reprogramar = models.DateField(blank=True, null=True)
    nombre = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=120, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguimiento'


class SentenciaConcialiacion(models.Model):
    codigo = models.AutoField(primary_key=True)
    sentencia = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'sentencia_concialiacion'


class SentenciaConciliacion(models.Model):
    codigo = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'sentencia_conciliacion'


class SubEstadonegociacion(models.Model):
    codigo = models.AutoField(primary_key=True)
    numeroestado = models.IntegerField(db_column='numeroEstado')  # Field name made lowercase.
    sub_estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sub_estadonegociacion'


class Subitemnegociacion(models.Model):
    codigo = models.AutoField(primary_key=True)
    subseguimiento = models.IntegerField(db_column='subSeguimiento')  # Field name made lowercase.
    seguimiento = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'subitemnegociacion'


class Subitemseguimiento(models.Model):
    codigo = models.AutoField(primary_key=True)
    subsegumiento = models.CharField(db_column='subSegumiento', max_length=30)  # Field name made lowercase.
    seguimiento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subitemseguimiento'


class Sucesiones(models.Model):
    codigo = models.IntegerField(primary_key=True)
    codreg = models.IntegerField(db_column='codReg')  # Field name made lowercase.
    sucesion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'sucesiones'


class TIdentificaciones(models.Model):
    codigo = models.IntegerField(primary_key=True)
    identificacion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 't_identificaciones'


class TMortalidad(models.Model):
    codigo = models.IntegerField(primary_key=True)
    edad = models.IntegerField(blank=True, null=True)
    sobrevivientes = models.IntegerField(blank=True, null=True)
    fallecidos = models.IntegerField(blank=True, null=True)
    p_sobrevivir = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    p_fallecer = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    esperanza = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    sexo = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mortalidad'


class Tasausura(models.Model):
    codigo = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    tasausura = models.FloatField(db_column='tasaUsura')  # Field name made lowercase.
    diaria = models.FloatField()
    diaria_dv_365 = models.FloatField(db_column='diaria_DV_365')  # Field name made lowercase.
    diaria_dv_360 = models.FloatField(db_column='diaria_DV_360')  # Field name made lowercase.
    diaria365 = models.FloatField()
    interes = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasausura'


class TipoContrato(models.Model):
    codigo = models.IntegerField(primary_key=True)
    tipo_contrato = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tipo_contrato'


class TipoSeguimiento(models.Model):
    codigo = models.AutoField(primary_key=True)
    seguimiento = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_seguimiento'


class Tipofallo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    subcategoria = models.CharField(max_length=45)
    fallo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipofallo'


class Vinculacionben(models.Model):
    codigo = models.IntegerField(primary_key=True)
    codreg = models.IntegerField(db_column='codReg')  # Field name made lowercase.
    documentoid = models.IntegerField(db_column='documentoId')  # Field name made lowercase.
    tipoid = models.IntegerField(db_column='tipoId')  # Field name made lowercase.
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fechanacimiento = models.DateField()
    estado_civil = models.IntegerField()
    nivel_academico = models.IntegerField()
    vivienda = models.IntegerField()
    ocupacion = models.IntegerField()
    tipo_contrato = models.IntegerField()
    fechaexpedicion = models.DateField(db_column='fechaExpedicion')  # Field name made lowercase.
    lugarexpedicion = models.IntegerField(db_column='lugarExpedicion')  # Field name made lowercase.
    nacionalidad = models.IntegerField()
    civilotro = models.CharField(db_column='civilOtro', max_length=150)  # Field name made lowercase.
    sexo = models.IntegerField()
    lugarnacimiento = models.IntegerField(db_column='lugarNacimiento')  # Field name made lowercase.
    personascargo = models.IntegerField(db_column='personasCargo')  # Field name made lowercase.
    celular = models.IntegerField()
    email = models.CharField(max_length=15)
    tipovivienda = models.IntegerField(db_column='tipoVivienda')  # Field name made lowercase.
    direccion = models.CharField(max_length=150)
    ciudad = models.IntegerField()
    barrio = models.CharField(max_length=150)
    estrato = models.IntegerField()
    telefono = models.IntegerField()
    profesion = models.IntegerField()
    otraocupacion = models.CharField(db_column='otraOcupacion', max_length=150)  # Field name made lowercase.
    empresa = models.CharField(max_length=150)
    cargo = models.CharField(max_length=150)
    ingresomensual = models.IntegerField(db_column='ingresoMensual')  # Field name made lowercase.
    fechaingreso = models.DateField(db_column='fechaIngreso')  # Field name made lowercase.
    ciiu = models.IntegerField()
    actividadeconomica = models.IntegerField(db_column='actividadEconomica')  # Field name made lowercase.
    emailempresa = models.CharField(db_column='emailEmpresa', max_length=150)  # Field name made lowercase.
    direccionempresa = models.CharField(db_column='direccionEmpresa', max_length=150)  # Field name made lowercase.
    ciudadempresa = models.IntegerField(db_column='ciudadEmpresa')  # Field name made lowercase.
    telefonoempresa = models.IntegerField(db_column='telefonoEmpresa')  # Field name made lowercase.
    extension = models.IntegerField()
    honorarios = models.IntegerField()
    vehiculo = models.IntegerField()
    otrosingresos = models.IntegerField(db_column='otrosIngresos')  # Field name made lowercase.
    totalingresos = models.IntegerField(db_column='totalIngresos')  # Field name made lowercase.
    arriendo = models.IntegerField()
    gastos = models.IntegerField()
    otrosgastos = models.IntegerField(db_column='otrosGastos')  # Field name made lowercase.
    totalegresos = models.IntegerField(db_column='totalEgresos')  # Field name made lowercase.
    desingresos = models.CharField(db_column='desIngresos', max_length=150)  # Field name made lowercase.
    activocasa = models.IntegerField(db_column='activoCasa')  # Field name made lowercase.
    activovehiculo = models.IntegerField(db_column='activoVehiculo')  # Field name made lowercase.
    acciones = models.IntegerField()
    otrosactivos = models.IntegerField(db_column='otrosActivos')  # Field name made lowercase.
    totalpasivo = models.IntegerField(db_column='totalPasivo')  # Field name made lowercase.
    patrimonio = models.IntegerField()
    declara = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vinculacionben'


class Vivienda(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre_vivienda = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'vivienda'
