from django.shortcuts import render

from rest_framework import viewsets
from .models import TreeNode, Tree
from .serializers import TreeNodeSerializer, TreeSerializer

class TreeNodeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing TreeNode instances.
    """
    serializer_class = TreeNodeSerializer
    queryset = TreeNode.objects.all()

class TreeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Tree instances.
    """
    serializer_class = TreeSerializer
    queryset = Tree.objects.all()
