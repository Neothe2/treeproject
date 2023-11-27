from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mytree.views import TreeNodeViewSet, TreeViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'treenodes', TreeNodeViewSet)
router.register(r'trees', TreeViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
