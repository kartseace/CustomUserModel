from django.urls import path
from . import views
urlpatterns=[
    path('',views.Home.as_view(),name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('services/', views.Services.as_view(), name='services'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('typo/', views.Typo.as_view(), name='typo'),
]