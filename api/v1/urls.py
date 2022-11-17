from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('/assets', include('api.v1.asset.urls')),
    path('/accounts', include('api.v1.account.urls')),
    path('/users', include('api.v1.user.urls')),
    path('/deposits', include('api.v1.deposit.urls')),
    path('/schema', SpectacularAPIView.as_view(), name='schema'),
    path('/swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
