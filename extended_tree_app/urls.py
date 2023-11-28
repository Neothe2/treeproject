from django.urls import path, include
from rest_framework.routers import DefaultRouter

from extended_tree_app.models import Tree1, Tree2
from extended_tree_app.serializers import Tree1Serializer, Tree2Serializer
from mytree.models import Tree
from mytree.serializers import TreeSerializer
from mytree.views import TreeNodeViewSet, TreeViewSet, customTreeViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'treenodes', TreeNodeViewSet)
router.register(r'trees', customTreeViewSet(TreeSerializer, Tree), basename='trees')
router.register(r'trees1', customTreeViewSet(Tree1Serializer, Tree1), basename='trees1')
router.register(r'trees2', customTreeViewSet(Tree2Serializer, Tree2), basename='trees2')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
