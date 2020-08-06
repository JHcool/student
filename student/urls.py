"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from studentapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listone/', views.listone), 
    path('listall/', views.listall), 
    path('index/', views.index), 
    path('forminitial/', views.forminitial), 

    path('post/', views.post), #傳送資料
    path('post1/', views.post1), #傳送資料不須驗證
    path('post2/', views.post2), #傳送資料需要驗證
    path('delete/', views.delete), 
    path('delete/<str:id>/', views.delete), 
    path('edit/', views.edit), 
    path('edit/<str:id>/', views.edit), 
]
