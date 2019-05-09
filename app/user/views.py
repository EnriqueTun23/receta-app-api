
from rest_framework import authentication, permissions
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UsuarioSerializer, AuthTokenSerializer
# Create your views here.
class CrearUsuarioView(CreateAPIView):
    """Crear un nuevo usuario en el sistema"""
    serializer_class = UsuarioSerializer


class CrearTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class AdministrarUsuarioView(RetrieveUpdateAPIView):
    """manage the authenticated user"""
    serializer_class = UsuarioSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """REtrive and return aunthentication"""

        return self.request.user