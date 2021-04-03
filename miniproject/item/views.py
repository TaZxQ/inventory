from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item
from rest_framework import viewsets


class ItemViewSet(viewsets.ModelViewSet):
    """
    This class is the view of all the endpoint related to items, post, get, patch and delete
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # managers can view only their items
        if not request.user.is_superuser:
            queryset = Item.objects.filter(batch__manager=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
