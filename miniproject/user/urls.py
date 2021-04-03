from django.urls import include, path
from .views import UserLoginApiView, LogoutApiView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'account', UserViewSet, basename="registrations")

urlpatterns = [
    path('login/', UserLoginApiView.as_view(), name="login"),
    path('logout/', LogoutApiView.as_view(), name="logout"),
    path('', include(router.urls)),
]
