import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'treeproject.settings')
django.setup()

from extended_tree_app.models import TreeNode1, Tree1, TreeNode2, Tree2
from django.contrib.contenttypes.models import ContentType

# node1 = TreeNode1(data='New Node1 this one will be parent', extra_data1='node 1 data')
# node1.save()
# # Create an instance of ExtendedTreeNode
# node2 = TreeNode2(data='New Node2 this one will be the child of node 1', extra_data2='node 2 data')
# node2.save()
#
# node1.add_child(node2)
#
# # Create an instance of ExtendedTree
# tree1 = Tree1(additional_info1='Extendetd tree Info')
# tree1.set_root_node(node1)  # Sets the extended_node as the root
# tree1.save()
#
# tree2 = Tree2(additional_info2='Extendetd tree Info')
# tree2.set_root_node(node2)  # Sets the extended_node as the root
# tree2.save()


tree1_root = TreeNode1(data='This is the root', extra_data1='This is the extradata1')
tree1_root.save()

tree1 = Tree1(root_node=tree1_root)
tree1.save()

tree_node1 = TreeNode1(data='tree_node1', extra_data1='extradata1 for treenode1')
tree_node2 = TreeNode1(data='tree_node2', extra_data1='extradata1 for treenode2')
tree_node3 = TreeNode1(data='tree_node3', extra_data1='extradata1 for treenode3')

tree_node1.save()
tree_node2.save()
tree_node3.save()

tree1.add_node(tree_node1, tree1_root)
tree1.add_node(tree_node2, tree1_root)
tree1.add_node(tree_node3, tree_node1)
