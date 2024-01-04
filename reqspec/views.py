from django.db import transaction
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from mytree.views import customTreeNodeViewSet
from reqspec.models import UseCaseDescription
from reqspec.serializers import UseCaseDescriptionSerializer


def customStepViewSet(serializer_class, model):

    class GenericStepViewSet(customTreeNodeViewSet(serializer_class, model)):
        pass


    return GenericStepViewSet


class UseCaseDescriptionViewSet(viewsets.ModelViewSet):
    queryset = UseCaseDescription.objects.all()
    serializer_class = UseCaseDescriptionSerializer

