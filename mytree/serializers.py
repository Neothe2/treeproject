from rest_framework import serializers
from .models import TreeNode, Tree

class TreeNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeNode
        fields = ['id', 'data', 'parent', 'children', 'forward_associations', 'backward_associations', 'order']


    children = serializers.SerializerMethodField()
    forward_associations = serializers.SerializerMethodField()
    backward_associations = serializers.SerializerMethodField()

    def get_children(self, obj):
        # This method will be used to serialize the children
        children = obj.children.all()  # Assuming 'children' is the related name in the model
        return TreeNodeSerializer(children, many=True).data

    def get_forward_associations(self, obj):
        # Use select_subclasses() to get instances of the specific subclasses
        associated_nodes = obj.forward_associations.all().select_subclasses()
        return [
            {"id": node.id, "url": type(node).url}
            for node in associated_nodes
        ]

    def get_backward_associations(self, obj):
        # Use select_subclasses() to get instances of the specific subclasses
        associated_nodes = obj.backward_associations.all().select_subclasses()
        return [
            {"id": node.id, "url": type(node).url}
            for node in associated_nodes
        ]

class TreeSerializer(serializers.ModelSerializer):
    root_node = TreeNodeSerializer(read_only=True)

    class Meta:
        model = Tree
        fields = ['id', 'root_node']


#Indent forward: Yes
#Indent backward: Yes
#Change order: Yes
#Editing: Yes
#Add: Yes