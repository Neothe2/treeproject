from rest_framework import serializers

from extended_tree_app.models import Tree1, Tree2, Tree3, TreeNode3
from mytree.serializers import TreeSerializer, TreeNodeSerializer


class Tree1Serializer(TreeSerializer):
    class Meta(TreeSerializer.Meta):
        model = Tree1


class Tree2Serializer(TreeSerializer):
    class Meta(TreeSerializer.Meta):
        model = Tree2


class TreeNode3Serializer(TreeNodeSerializer):
    children = serializers.SerializerMethodField()
    # extra_data3 = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)


    def get_children(self, obj):
        # This method will be used to serialize the children
        children = obj.children.all()  # Assuming 'children' is the related name in the model
        return TreeNode3Serializer(children, many=True).data

    class Meta(TreeNodeSerializer.Meta):
        model = TreeNode3
        fields = TreeNodeSerializer.Meta.fields + ['extra_data3']


class Tree3Serializer(TreeSerializer):
    root_node = TreeNode3Serializer(read_only=True)

    class Meta(TreeSerializer.Meta):
        model = Tree3


