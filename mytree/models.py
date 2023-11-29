from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

# Create your models here.
class TreeNode(models.Model):
    data = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    forward_associations = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='backward_associations',
        blank=True
    )


# Signal receiver to update backward associations


    def add_child(self, child_node):
        # Ensure the child_node is a TreeNode instance
        if not isinstance(child_node, TreeNode):
            raise ValueError("child_node must be an instance of TreeNode")

        # Disassociate the child_node from any existing parent or tree
        if child_node.parent:
            child_node.parent = None
        child_node.save()

        # Set the child_node's parent to self and save
        child_node.parent = self
        child_node.save()

    def __str__(self):
        return self.data

@receiver(m2m_changed, sender=TreeNode.forward_associations.through)
def update_backward_associations(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == "post_add":
        if not reverse:
            # Forward association added, update backward associations
            for pk in pk_set:
                associated_node = model.objects.get(pk=pk)
                associated_node.backward_associations.add(instance)
        else:
            # Backward association added, update forward associations
            for pk in pk_set:
                associated_node = model.objects.get(pk=pk)
                associated_node.forward_associations.add(instance)


class Tree(models.Model):
    root_node = models.OneToOneField(TreeNode, on_delete=models.CASCADE, related_name='tree')

    def __init__(self, *args, root_node=None, **kwargs):
        super().__init__(*args, **kwargs)
        if root_node is not None:
            self.set_root_node(root_node)

    # def save(self, *args, **kwargs):
    #     if not self.root_node_id:
    #         # Automatically create a new TreeNode as the root if not already set
    #         root_node = TreeNode.objects.create(data="Root Node")
    #         self.root_node = root_node
    #     super().save(*args, **kwargs)

    def set_root_node(self, node):
        if not isinstance(node, TreeNode):
            raise ValueError("node must be an instance of TreeNode or its subclass")

        # Check if a Tree already exists with this node as root
        if Tree.objects.filter(root_node=node).exists():
            raise ValidationError("This node is already set as a root for another tree")

        self.root_node = node
        self.save()

    def add_node(self, node, under):
        if not isinstance(node, TreeNode):
            raise ValueError("node must be an instance of TreeNode or its subclass")

        if not isinstance(under, TreeNode):
            raise ValueError("under must be an instance of TreeNode or its subclass")

        under.add_child(node)

    def __str__(self):
        return f'Tree with root: {self.root_node}'

