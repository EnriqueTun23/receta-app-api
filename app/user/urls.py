from django.urls import path

from .views import CrearUsuarioView, CrearTokenView

app_name = 'user'

urlpatterns = [
    path('create/', CrearUsuarioView.as_view(), name='create'),
    path('token/', CrearTokenView.as_view(), name='token'),
]