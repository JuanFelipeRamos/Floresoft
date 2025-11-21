from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TypeVariedadFlorViewSet, VariedadFlorViewSet

router = DefaultRouter()

router.register(r'variedad_flor', VariedadFlorViewSet, basename="variedad-flor")
router.register(r'type_variedad_flor', TypeVariedadFlorViewSet, basename="type-variedad-flor")

urlpatterns = [
    path('', include(router.urls)),
]
