from django.urls import path,include
from rest_framework import routers
from .views import PersonViewSet,Person1ViewSet


router = routers.DefaultRouter()
router.register(r'person',PersonViewSet)
router.register(r'person1',Person1ViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls'))
]
