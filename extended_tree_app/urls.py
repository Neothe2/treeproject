from django.urls import path, include
from rest_framework.routers import DefaultRouter

from extended_tree_app.models import Tree1, Tree2, TreeNode1, TreeNode2, TreeNode3, Tree3
from extended_tree_app.serializers import Tree1Serializer, Tree2Serializer, Tree3Serializer, TreeNode3Serializer
from mytree.models import Tree, TreeNode
from mytree.serializers import TreeSerializer, TreeNodeSerializer
from mytree.views import TreeNodeViewSet, TreeViewSet, customTreeViewSet, customTreeNodeViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'treenodes', TreeNodeViewSet)
router.register(r'treenodes3', customTreeNodeViewSet(TreeNode3Serializer, TreeNode3), basename='treenode3')
router.register(r'trees', customTreeViewSet(TreeSerializer, Tree, TreeNode), basename='trees')
router.register(r'trees1', customTreeViewSet(Tree1Serializer, Tree1, TreeNode1), basename='trees1')
router.register(r'trees2', customTreeViewSet(Tree2Serializer, Tree2, TreeNode2), basename='trees2')
router.register(r'trees3', customTreeViewSet(Tree3Serializer, Tree3, TreeNode3), basename='trees3')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

