from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaMaterialViewSet, MaterialViewSet

router = DefaultRouter()

router.register('material', MaterialViewSet, basename="material")
router.register('categoria_material', CategoriaMaterialViewSet, basename="categoria_material")

urlpatterns = [
    path('', include(router.urls)),
]
