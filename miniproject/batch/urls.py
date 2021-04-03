# Local imports
from .views import BatchViewSet

# Django imports
from django.urls import include, path

# RestFramework imports
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BatchViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
