from ipercAPI.models import Iperc, Usuario, Area
from ipercAPI.serializers import IpercSerializer, IpecByDateSerializer
from datetime import datetime

from rest_framework import views,generics

class IpercList(generics.ListCreateAPIView):
	queryset = Iperc.objects.all()
	serializer_class = IpercSerializer


class IpercByUser(generics.ListAPIView):

	serializer_class = IpercSerializer

	def get_queryset(self):
		pk = self.kwargs['pk']
		usuario = Usuario.objects.get(pk = pk)

		iperc = Iperc.objects.filter(usuario = usuario)
		return iperc


class IpercByDate(generics.ListAPIView):

	serializer_class = IpercSerializer

	def get_queryset(self):
		start = self.kwargs['start']
		end = self.kwargs['end']
		start = datetime.strptime(start,'%Y-%m-%d').strftime("%m/%d/%y")
		start = datetime.strptime(start,"%m/%d/%y")
		
		end = datetime.strptime(end,'%Y-%m-%d').strftime("%m/%d/%y")
		end = datetime.strptime(end,"%m/%d/%y")

		iperc = Iperc.objects.filter(created_at__range=(start, end))

		return iperc

class IpercByArea(generics.ListAPIView):
	serializer_class = IpercSerializer

	def get_queryset(self):
		area = self.kwargs['area']
		area = Area.objects.get(pk = area)

		iperc = Iperc.objects.filter(area = area)
		return iperc