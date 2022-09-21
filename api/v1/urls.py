from django.urls import path, include

urlpatterns = [
    path('/assets', include('api.v1.asset.urls')),
    path('/accounts', include('api.v1.account.urls')),
    path('/users', include('api.v1.user.urls')),
    path('/deposits', include('api.v1.deposit.urls')),
]
