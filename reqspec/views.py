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
        @action(detail=False, methods=['post'])
        def set_order(self, request):
            step_orders = request.data  # Expecting format: { "20": 1, "21": 2, "32": 3 }
            try:
                with transaction.atomic():
                    for step_id, order in step_orders.items():
                        model.objects.filter(id=step_id).update(order=order)
                return Response({"message": "Step orders updated successfully."})
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    return GenericStepViewSet


class UseCaseDescriptionViewSet(viewsets.ModelViewSet):
    queryset = UseCaseDescription.objects.all()
    serializer_class = UseCaseDescriptionSerializer

