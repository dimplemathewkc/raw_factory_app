from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .api import InventoryApi
router = DefaultRouter()
router.register(r'api/v1/inventory', InventoryApi)
urlpatterns = [

]

urlpatterns += router.urls