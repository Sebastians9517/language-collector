from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('languages/', views.languages_index, name='index'),
    path('languages/create/', views.LanguagesCreate.as_view(), name='create'),
    path('languages/<int:pk>/update/', views.LanguagesUpdate.as_view(), name='update'),
    path('languages/<int:pk>/delete/', views.LanguagesDelete.as_view(), name='delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
