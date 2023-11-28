from extended_tree_app.models import Tree1, Tree2
from mytree.serializers import TreeSerializer


class Tree1Serializer(TreeSerializer):
    class Meta(TreeSerializer.Meta):
        model = Tree1


class Tree2Serializer(TreeSerializer):
    class Meta(TreeSerializer.Meta):
        model = Tree2
