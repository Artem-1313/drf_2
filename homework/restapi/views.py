from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .serializer import StoreSerializer
from .models import Store


class StoreAPI(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class MyStores(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
       print(self.request.auth)
       serializer.save(**{'owner': self.request.user})
