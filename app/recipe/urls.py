from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TagViewSet, IngredienteViewSet

router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('ingredients', IngredienteViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]