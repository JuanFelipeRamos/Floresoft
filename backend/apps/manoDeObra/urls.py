from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManoDeObraViewSet, CostoVariedadTinturarViewSet

router = DefaultRouter()

router.register('mano_de_obra', ManoDeObraViewSet, basename="mano_de_obra")
router.register('costo_variedad_tinturar', CostoVariedadTinturarViewSet, basename="costo-variedad-tinturar")

urlpatterns = [
    path('', include(router.urls))
]
