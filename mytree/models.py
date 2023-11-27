from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError

# Create your models here.
class TreeNode(models.Model):
    data = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.data


class Tree(models.Model):
    root_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    root_object_id = models.PositiveIntegerField(null=True, blank=True)
    root_node = GenericForeignKey('root_content_type', 'root_object_id')

    def set_root_node(self, node):
        if not isinstance(node, TreeNode) or type(node) is TreeNode:
            raise ValueError("node must be an instance of a TreeNode subclass")

        # Check if a Tree already exists with this node as root
        if Tree.objects.filter(root_content_type=ContentType.objects.get_for_model(type(node)), root_object_id=node.id).exists():
            raise ValidationError("This node is already set as a root for another tree")

        self.root_content_type = ContentType.objects.get_for_model(type(node))
        self.root_object_id = node.id
        self.save()

    def __str__(self):
        return f'Tree with root: {self.root_node}'
