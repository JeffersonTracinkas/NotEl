from django.conf.urls import include, url
from usuarios import views
from views import RegistrarView

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url':'/login/'}, name='logout'),
    url(r'^registrar/$', RegistrarView.as_view(), name='registrar'),
    url(r'^usuario/$', views.usuario, name='usuario'),
    url(r'^usuario/editar$', views.usuario_editar, name='usuario_editar')
]
