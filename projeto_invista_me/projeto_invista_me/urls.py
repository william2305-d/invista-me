"""
URL configuration for projeto_invista_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invista_me import views
from user import views as user_views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', user_views.novo_usuario, name='novo_usuario'),
    #path('logout/', TemplateView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('', views.investimentos, name='investimentos'),
    path('contato/', views.pagina_contato, name='contato'),
    path('minha_historia/', views.minha_historia, name='minha_historia'),
    path('novo_investimento/',views.criar, name='novo_investimento'),
    path('investimento_registrado/',views.investimento_registrado, name='investimento_registrado'),
    path('/<int:id_investimento>', views.detalhe, name='detalhe'),
    path('novo_investimento/<int:id_investimento>', views.editar, name='editar'),
    path('excluir_ivestimento/<int:id_investimento>', views.excluir, name='excluir')
]
