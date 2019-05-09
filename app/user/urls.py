from django.urls import path

from .views import CrearUsuarioView, CrearTokenView, AdministrarUsuarioView

app_name = 'user'

urlpatterns = [
    path('create/', CrearUsuarioView.as_view(), name='create'),
    path('token/', CrearTokenView.as_view(), name='token'),
    path('me/', AdministrarUsuarioView.as_view(), name='me'),
]