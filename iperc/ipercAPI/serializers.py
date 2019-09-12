import datetime
from rest_framework import serializers
from ipercAPI.models import Area, Labor, Usuario, Peligro, Riesgo, Iperc


class AreaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Area
		fields = '__all__'


class LaborSerializer(serializers.ModelSerializer):
	class Meta:
		model = Labor
		fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = '__all__'


class PeligroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Peligro
		fields = '__all__'


class RiesgoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Riesgo
		fields = '__all__'

class IpercSerializer(serializers.ModelSerializer):
	class Meta:
		model = Iperc
		fields = '__all__'

class IpecByDateSerializer(serializers.ModelSerializer):
	start = serializers.DateField(initial=datetime.date.today)
	end = serializers.DateField(initial=datetime.date.today)

	class Meta:
		model = Iperc
		fields = ('start','end')