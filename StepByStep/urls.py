from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from Account.views import UserViewSet, SessionApiView
from Area.views import AreaViewSet
from Plan.views import PlanViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('area', AreaViewSet)
router.register('plan', PlanViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/session/', SessionApiView.as_view()),

    # jwt
    path('api/token/', obtain_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),

    # admin
    path('admin/', admin.site.urls),
]
