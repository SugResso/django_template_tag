from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_chapters),
    path('<str:name_menu>/', views.get_sub_chapters, name='sub_chapter'),
]