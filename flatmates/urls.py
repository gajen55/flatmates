from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.template import loader

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

app_name='flatmates'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.my_logout, name='logout'),
    url(r'^add/$', views.AddExpense.as_view(), name='add'),
    url(r'^view/$',views.ViewExpense.as_view(), name='view'),
    url(r'^profile/$', views.Profile.as_view(), name = 'profile'),
    url(r'^edit/$', views.EditEntries.as_view(), name='edit'),
    url(r'^change_password/$', views.ChangePassword.as_view(),name='change_password'),
]