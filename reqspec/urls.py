from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .models import MainFlow, AlternateFlow, ExceptionFlow, MainFlowStep, AlternateFlowStep, ExceptionFlowStep
from .serializers import MainFlowStepSerializer, AlternateFlowStepSerializer, ExceptionFlowStepSerializer, ExceptionFlowSerializer, AlternateFlowSerializer, MainFlowSerializer
from mytree.models import Tree, TreeNode
from mytree.serializers import TreeSerializer, TreeNodeSerializer
from mytree.views import TreeNodeViewSet, TreeViewSet, customTreeViewSet, customTreeNodeViewSet
from .views import customStepViewSet, UseCaseDescriptionViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(MainFlowStep.url, customStepViewSet(MainFlowStepSerializer, MainFlowStep))
router.register(AlternateFlowStep.url, customStepViewSet(AlternateFlowStepSerializer, AlternateFlowStep))
router.register(ExceptionFlowStep.url, customStepViewSet(ExceptionFlowStepSerializer, ExceptionFlowStep))
router.register(r'main_flows', customTreeViewSet(MainFlowSerializer, MainFlow, MainFlowStep))
router.register(r'alternate_flows', customTreeViewSet(AlternateFlowSerializer, AlternateFlow, AlternateFlowStep))
router.register(r'exception_flows', customTreeViewSet(ExceptionFlowSerializer, ExceptionFlow, ExceptionFlowStep))
router.register(r'use_case_descriptions', UseCaseDescriptionViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

