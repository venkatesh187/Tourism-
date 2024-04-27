"""
URL configuration for thmsproject project.

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('provhome', views.provhomefn, name="provhome"),
    path('provlogin', views.provloginfn, name="provlogin"),
    path('provregister', views.provregisterfn, name="provregister"),
    path('provhotel', views.provhotelfn, name="provhotel"),
    path('provservices', views.provservicesfn, name="provservices"),
    path('provplaces', views.provplacesfn, name="provplaces"),
    path("provfeedback", views.provfeedbackfn, name="provfeedback"),
    path("provlogout", views.provlogoutfn, name="provlogout"),
    path("checkprovlogin",views.checkprovlogin,name="checkprovlogin"),
    path("viewservices",views.viewservicesfn,name="viewservices"),
    path("addservices",views.addservicesfn,name="addservices"),
    path("insertservices",views.insertservicefn,name="insertservices"),
    path("deleteservice",views.deleteservicefn,name="deleteservice"),
    path("servicedeletion/<int:sid>",views.servicedeletion,name="servicedeletion"),
    path("addplaces",views.addplacesfn,name="addplaces"),
    path("insertplaces",views.insertplacesfn,name="insertplaces"),
    path("viewplaces",views.viewplacesfn,name="viewplaces"),
    path("inserthotel",views.inserthotelfn,name="inserthotel"),
    path("registerhotel",views.registerhotelmanagerfn,name="registerhotel")


]
