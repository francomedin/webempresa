from django.urls import path
from . import views


urlpatterns = [
    # Paths del Core
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    

]
