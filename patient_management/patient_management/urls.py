"""
URL configuration for patient_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from patient_management_app.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from patient_management_app.views import CustomAuthenticationForm

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapi.com/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('login_view/', login_view, name='login_view'),
    path('', login_view, name='login'),

    path('home/', home, name='home'),
    path('edit_bulletin/<int:bulletin_id>/', edit_bulletin, name='edit_bulletin'),
    path('add_bulletin/', add_bulletin, name='add_bulletin'),
    path('delete_bulletin/<int:bulletin_id>/', delete_bulletin, name='delete_bulletin'),

    path('patients/', patient_list, name='patient_list'),
    path('edit_patient/<int:patient_id>/', edit_patient, name='edit_patient'),
    path('add_patient/', add_patient, name='add_patient'),
    path('delete_patient/<int:patient_id>/', delete_patient, name='delete_patient'),

    path('staffs/', staff_list, name='staff_list'),
    path('edit_staff/<int:staff_id>/', edit_staff, name='edit_staff'),
    path('add_staff/', add_staff, name='add_staff'),
    path('delete_staff/<int:staff_id>/', delete_staff, name='delete_staff'),
]
