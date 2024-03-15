from django.urls import path
from . import views
urlpatterns = [
    path('', views.meno, name='meno'),
    path('list/<str:hazrat>/', views.meno2, name='meno2'),
    path('list/<str:hazrat>/create', views.create, name='create'),
    path('madahy/<int:id>', views.madahy2, name='madahy'),


]