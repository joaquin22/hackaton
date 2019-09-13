from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Peligro(models.Model):
	nombre_peligro = models.CharField(max_length=30, null=False,blank=False)

class Riesgo(models.Model):
	nombre_riesgo = models.CharField(max_length=30, blank=False, null=False)
	peligro = models.ForeignKey(Peligro,on_delete=models.CASCADE,related_name='riesgo_peligro')


class Area(models.Model):
	nombre_area = models.CharField(max_length=30, blank=False, null=False)

class Labor(models.Model):
	descripcion = models.CharField(max_length=100, blank=False, null=False)
	area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='labor_area')


class Usuario(User):
	ADMIN = 0
	OBRERO = 1
	ROLES = (
		(ADMIN,'Administrdor'),
		(OBRERO,'Obrero')
	)
	codigo = models.CharField(max_length=30, blank=False, null=False)
	cargo = models.CharField(max_length=30, blank=False, null=False)
	rol = models.IntegerField(null=True, default=0, choices=ROLES)
	celular = models.CharField(blank=True, null=True,max_length=10)
	area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='usuario_area')

class Iperc(models.Model):

	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='iperc_usuario')
	area = models.ForeignKey(Area, on_delete=models.CASCADE,related_name='iperc_area')
	labor = models.ForeignKey(Labor, on_delete=models.CASCADE,related_name='iperc_labor')
	peligro = models.ForeignKey(Peligro, on_delete=models.CASCADE,related_name='iperc_peligro')
	riesgo = models.ForeignKey(Riesgo, on_delete=models.CASCADE,related_name='iperc_riesgo')
	puntaje = models.IntegerField(blank=False, null=False)
	firma = models.ImageField(upload_to='firma_digital', null=True, blank= True)
	foto_reporte = models.ImageField(upload_to='foto_reporte', null=True, blank= True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)