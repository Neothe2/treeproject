from django.db import models

from mytree.models import TreeNode, Tree


# Create your models here.
class TreeNode1(TreeNode):
    extra_data1 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'treenode1'


class TreeNode2(TreeNode):
    extra_data2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'treenode2'


class Tree1(Tree):
    pass


class Tree2(Tree):
    pass
