from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LostItemsViewset, FoundItemViewset, ClaimViewSet, UserViewSet
from . import views
router = DefaultRouter()
router.register(r"lost-items", views.LostItemsViewset, basename='lostitems')
router.register(r"found-items", views.FoundItemViewset, basename='founditem')
router.register(r'users', UserViewSet, basename='user')
router.register(r'claims', ClaimViewSet)
urlpatterns = [
    path('', include(router.urls)),
  
    
]