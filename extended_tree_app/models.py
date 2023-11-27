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
    additional_info1 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'ExtendedTree with root: {self.root.data} and info: {self.additional_info1}'


class Tree2(Tree):
    additional_info2 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'ExtendedTree with root: {self.root.data} and info: {self.additional_info2}'
