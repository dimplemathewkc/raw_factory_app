from rest_framework import viewsets
from .models import Item, Quantity, Inventory
from .serializer import InventorySerializer


class InventoryApi(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer