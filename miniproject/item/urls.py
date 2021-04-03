from .views import ItemViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', ItemViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
