from ipercAPI.models import Area, Labor
from ipercAPI.serializers import AreaSerializer, LaborSerializer
from rest_framework import views, generics


class AreaList(generics.ListCreateAPIView):
	queryset = Area.objects.all()
	serializer_class = AreaSerializer


class LaborList(generics.ListCreateAPIView):
	queryset = Labor.objects.all()
	serializer_class = LaborSerializer
