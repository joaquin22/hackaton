from ipercAPI.models import Peligro, Riesgo
from rest_framework import views, generics
from ipercAPI.serializers import PeligroSerializer, RiesgoSerializer

class PeligroList(generics.ListCreateAPIView):
	queryset = Peligro.objects.all()
	serializer_class = PeligroSerializer


class RiesgoList(generics.ListCreateAPIView):
	queryset = Riesgo.objects.all()
	serializer_class = RiesgoSerializer
