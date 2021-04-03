from rest_framework.exceptions import NotAcceptable
from .models import UserAccount
from .serializers import UserSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not request.user.is_superuser:
            queryset = UserAccount.objects.filter(id=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # users other than admin/superuser can not perform this action
        if not request.user.is_superuser:
            raise PermissionDenied

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        # users other than admin/superuser can not perform this action
        if not request.user.is_superuser:
            raise PermissionDenied
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        # users other than admin/superuser can not perform this action
        if not request.user.is_superuser:
            raise PermissionDenied
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication tokens """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        # delete old token and assign a new one for evey login request
        if not created:
            token.delete()
            token = Token.objects.create(user=user)

        return Response(
            {
                'token': token.key,

                'first_name': token.user.first_name,
                'last_name': token.user.last_name,
                'created_at': token.user.date_joined,

            }
        )


class LogoutApiView(APIView):
    """Handles logout"""

    def post(self, request):
        print(request.user.email)
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
