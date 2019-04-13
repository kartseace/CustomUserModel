
from django.contrib import admin
from django.urls import path,include
from users.views import register, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('portal.urls')),
    path(r'^register/$', register),
    path(r'^login/$', login_view),
    path(r'^logout/$', logout_view)]
