from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),

    path('api/token/', obtain_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),

    path('admin/', admin.site.urls),
]
