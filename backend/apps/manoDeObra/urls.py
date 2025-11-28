from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManoDeObraViewSet

router = DefaultRouter()

router.register('mano_de_obra', ManoDeObraViewSet, basename="mano_de_obra")

urlpatterns = [
    path('', include(router.urls))
]
