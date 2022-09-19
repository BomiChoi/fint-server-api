from django.urls import path, include

urlpatterns = [
    path('/assets', include('api.v1.asset.urls')),
]
