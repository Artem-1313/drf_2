from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import StoreSerializer
from .models import Store


class StoreAPI(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class MyStores(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(**{'owner': self.request.user})

    @action(methods=['post'], detail=True)
    def mark_as_active(self, request, pk=None):
        store = self.get_object()

        if store.status == 'deactivated':
            store.status = 'active'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def mark_as_deactivated(self, request, pk=None):
        store = self.get_object()
        if store.status == 'active':
            store.status = 'deactivated'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)

class AdminStores(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


    @action(methods=['post'], detail=True)
    def mark_as_active(self, request, pk=None):
        store = self.get_object()
        if store.status == 'in_review':
            store.status = 'active'
            store.save()
        if store.status == 'deactivated':
            store.status = 'active'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)


    @action(methods=['post'], detail=True)
    def mark_as_deactivated(self, request, pk=None):
        store = self.get_object()
        if store.status == 'active':
            store.status = 'deactivated'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)


