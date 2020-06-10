from .models import Quantity,Inventory,Item
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','item_name')


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ('id','amount','quantity_type',)


class InventorySerializer(serializers.ModelSerializer):
    item_name = ItemSerializer()
    quantity = QuantitySerializer()

    class Meta:
        model = Inventory
        fields = ('item_name', 'quantity', 'price', 'unit',)