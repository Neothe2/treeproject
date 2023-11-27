from django.contrib import admin

# Registering the model for Django admin (optional, only if you have an admin.py in the same directory)
from django.contrib import admin

from extended_tree_app.models import TreeNode1, TreeNode2

admin.site.register(TreeNode1)
admin.site.register(TreeNode2)
