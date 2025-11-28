from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/usuarios/', include('apps.usuarios.urls')),
    path('api/flores/', include('apps.variedadFlor.urls')),
    path('api/materiales/', include('apps.materiales.urls')),
    path('api/manos_de_obra/', include('apps.manoDeObra.urls')),
    path('api/recetas/', include('apps.recetas.urls')),
]
