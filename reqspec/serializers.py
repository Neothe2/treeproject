from mytree.serializers import TreeSerializer, TreeNodeSerializer
from reqspec.models import MainFlow, AlternateFlow, ExceptionFlow, ExceptionFlowStep, AlternateFlowStep, MainFlowStep, \
    UseCaseDescription
from rest_framework import serializers


class MainFlowSerializer(TreeSerializer):
    class Meta(TreeSerializer.Meta):
        model = MainFlow


class AlternateFlowSerializer(TreeSerializer):
    class Meta(TreeSerializer.Meta):
        model = AlternateFlow


class ExceptionFlowSerializer(TreeSerializer):
    class Meta(TreeSerializer.Meta):
        model = ExceptionFlow


class MainFlowStepSerializer(TreeNodeSerializer):
    class Meta(TreeNodeSerializer.Meta):
        model = MainFlowStep


class AlternateFlowStepSerializer(TreeNodeSerializer):
    class Meta(TreeNodeSerializer.Meta):
        model = AlternateFlowStep


class ExceptionFlowStepSerializer(TreeNodeSerializer):
    class Meta(TreeNodeSerializer.Meta):
        model = ExceptionFlowStep


class UseCaseDescriptionSerializer(serializers.ModelSerializer):
    main_flow = serializers.PrimaryKeyRelatedField(queryset=MainFlow.objects.all(), allow_null=True)
    class Meta:
        model = UseCaseDescription
        fields = ['id', 'main_flow', 'alternate_flows', 'exception_flows']
