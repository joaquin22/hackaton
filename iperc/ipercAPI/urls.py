from django.conf.urls import url, include

from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token   
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework.documentation import include_docs_urls

from rest_framework.urlpatterns import format_suffix_patterns
from ipercAPI import views


urlpatterns = [
	url(r'^docs/', include_docs_urls(title='Iperc API')),
	url(r'^areas/$', views.AreaList.as_view()),
	url(r'^labor/$', views.LaborList.as_view()),
	url(r'^usuarios/$', views.UsuarioCreate.as_view()),
	url(r'^usuario/$', views.UsuarioByToken.as_view()),
	url(r'^peligro/$', views.PeligroList.as_view()),
	url(r'^riesgo/$', views.RiesgoList.as_view()),
	url(r'^iperc/$', views.IpercList.as_view()),
	url(r'^iperc/(?P<pk>[0-9]+)/', views.IpercByUser.as_view()),
	url(r'^iperc/area/(?P<area>[0-9]+)/', views.IpercByArea.as_view()),
	url(r'^iperc/fecha/(?P<start>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/(?P<end>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/$', views.IpercByDate.as_view()),
]

urlpatterns += [
	url(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns += [
	url(r'^api-token-auth/', obtain_jwt_token),
	url(r'^api-token-refresh/', refresh_jwt_token),
	url(r'^api-token-verify/', verify_jwt_token),

]

urlpatterns = format_suffix_patterns(urlpatterns)