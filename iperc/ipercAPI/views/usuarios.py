import random, string

from ipercAPI.models import Usuario
from ipercAPI.serializers import UsuarioSerializer

from rest_framework import generics, views, permissions
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.hashers import PBKDF2PasswordHasher

class UsuarioCreate(generics.ListCreateAPIView):
	
	serializer_class = UsuarioSerializer

	def post(self, request, *args, **kwargs):
		serialized = UsuarioSerializer(data=request.data)
		if serialized.is_valid(raise_exception=True):
			Usuario.objects.create_user(
				first_name = serialized.validated_data['first_name'],
				last_name= serialized.validated_data['last_name'],
				codigo = serialized.validated_data['codigo'],
				cargo = serialized.validated_data['cargo'],
				area = serialized.validated_data['area'],
				email = serialized.validated_data['email'],
				username = serialized.validated_data['username'],
				password = serialized.validated_data['password']
			)
			return Response(serialized.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

	queryset = Usuario.objects.all()



class UsuarioByToken(views.APIView):
	"""
	post:
	Retorna los datos de un usuario que ya este logeado
	"""
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def post(self, request, *args, **kwargs):
		user = Usuario.objects.filter(pk = request.user.id).first()

		return Response({"id": request.user.id,
											"first_name": request.user.first_name,
											"last_name": request.user.last_name,
											"email": request.user.email,
											"codigo" : user.codigo,
											"cargo":user.cargo,
											"area":user.area})
