import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'treeproject.settings')
django.setup()

from extended_tree_app.models import TreeNode1, Tree1, TreeNode2, Tree2
from django.contrib.contenttypes.models import ContentType

node1 = TreeNode1(data='New Node1', extra_data1='node 1 data')
node1.save()
# Create an instance of ExtendedTreeNode
node2 = TreeNode2(data='New Node2', extra_data2='node 2 data')
node2.save()

# Create an instance of ExtendedTree
tree1 = Tree1(additional_info1='Extendetd tree Info')
tree1.set_root_node(node1)  # Sets the extended_node as the root
tree1.save()

tree2 = Tree2(additional_info2='Extendetd tree Info')
tree2.set_root_node(node2)  # Sets the extended_node as the root
tree2.save()
