"""
URL configuration for Website project.

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
from django.urls import path,include
from Website import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage,name="home"),
    path('work/', views.Work,name="work"),
    path('login/', views.Login,name="login"),
    path('signin/', views.Signin,name="signin"),
    path('signup/', views.Signup,name="signup"),
    path('signout/', views.Signout,name="signout"),
    path('contact/', views.contact,name="contact"),
    path('about/', views.about,name="about"),
    path('form/', views.form,name="form"),
    path('table/<int:service_id>/', views.table,name="table"),
    path('tableForm/<int:service_id>/', views.tableForm,name="tableForm"),
    path('delete/<int:service>',views.Delete,name="delete"),
    path('sdelete/<int:service>',views.SDelete,name="sdelete"),
    path('update/<int:service>',views.Update,name="update"),
    path('updated_data/<int:service>',views.Updated_data,name="updated_data")
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)