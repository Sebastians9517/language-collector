from django.urls import path
from . import views

urlpatterns = [
    path('', views.LanguagesList.as_view(), name='index'),
    path('languages/create/', views.LanguagesCreate.as_view(), name='create'),
    path('languages/<int:pk>/update/', views.LanguagesUpdate.as_view(), name='update'),
    path('languages/<int:pk>/delete/', views.LanguagesDelete.as_view(), name='delete'),
]
