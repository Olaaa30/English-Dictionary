from django.urls import path
from dictionary import views
urlpatterns = [
  path('', views.index, name='index'),
  path('docs/', views.docs, name='docs')
]