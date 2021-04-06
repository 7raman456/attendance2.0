"""attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,re_path
from stubase import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.front),
    path('run',views.run),
    path('master',views.master),
    path('addstu/<slug:classs>',views.addstu),
    path('removestu/<slug:classs>',views.removestu),
    path('attendents/<slug:classs>',views.attendents),
    path('attendance/<slug:classs>',views.attendance),

]
