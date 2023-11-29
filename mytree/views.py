from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import TreeNode, Tree
from .serializers import TreeNodeSerializer, TreeSerializer

class TreeNodeViewSet(viewsets.ModelViewSet):
    serializer_class = TreeNodeSerializer
    queryset = TreeNode.objects.all()

    @action(detail=True, methods=['post'])
    def add_child(self, request, pk=None):
        parent_node = self.get_object()
        child_data = request.data
        child_serializer = self.get_serializer(data=child_data)

        if child_serializer.is_valid():
            child_node = child_serializer.save()
            parent_node.add_child(child_node)
            return Response(child_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(child_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TreeViewSet(viewsets.ModelViewSet):
    serializer_class = TreeSerializer
    queryset = Tree.objects.all()



    @action(detail=True, methods=['post'])
    def add_node(self, request, pk=None):
        tree = self.get_object()
        node_text = request.data.get('node')
        under_id = request.data.get('under')

        try:
            under_node = TreeNode.objects.get(pk=under_id)
        except TreeNode.DoesNotExist:
            return Response({'error': 'TreeNode with the given ID does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # Create a new TreeNode with the given text and add it under the 'under_node'
        new_node = TreeNode.objects.create(data=node_text)
        under_node.add_child(new_node)

        return Response({'status': 'Node added successfully'}, status=status.HTTP_200_OK)



from rest_framework import viewsets
from django.contrib.contenttypes.models import ContentType
from .models import Tree
from .serializers import TreeSerializer

# class GenericTreeViewSet(viewsets.ModelViewSet):
#
#     def __init__(self, *args, **kwargs):
#         self.serializer_class = kwargs.pop('serializer_class', TreeSerializer)
#         self.model = kwargs.pop('model', Tree)  # Default to Tree if no model is specified
#         super().__init__(*args, **kwargs)
#
#     def get_queryset(self):
#         return self.model.objects.all()
#
#     def perform_create(self, serializer):
#         # Dynamically determine the model class
#         model = self.model
#
#         # Ensure the model is a subclass of Tree
#         if not issubclass(model, Tree):
#             raise ValidationError("Invalid model type")
#
#         # Create an instance of the correct model
#         instance = model(**serializer.validated_data)
#         instance.save()

# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.exceptions import ValidationError
# from .models import TreeNode, Tree

def customTreeViewSet(serializer_class, model, tree_node_model):
    class GenericTreeViewSet(viewsets.ModelViewSet):
        def get_serializer_class(self):
            return serializer_class

        def get_model(self):
            return model

        def get_queryset(self):
            return self.get_model().objects.all()

        def perform_create(self, serializer):
            # Dynamically determine the model class
            model = self.get_model()

            # Ensure the model is a subclass of Tree
            if not issubclass(model, Tree):
                raise ValidationError("Invalid model type")

            # Create an instance of the correct model
            instance = model(**serializer.validated_data)

            # Create a new root node if it doesn't exist
            if not hasattr(instance, 'root_node') or instance.root_node is None:
                newroot = tree_node_model.objects.create(data='Root Node')
                instance.root_node = newroot
                instance.save()

            instance.save()


        @action(detail=True, methods=['post'])
        def add_node(self, request, pk=None):
            tree = self.get_object()
            node_data = request.data.get('node')
            under_id = request.data.get('under')

            try:
                under_node = TreeNode.objects.get(pk=under_id)
            except TreeNode.DoesNotExist:
                return Response({'error': 'TreeNode with the given ID does not exist.'},
                                status=status.HTTP_404_NOT_FOUND)

            # Create a new TreeNode with the unpacked node_data
            new_node = tree_node_model.objects.create(**node_data)
            under_node.add_child(new_node)

            return Response({'status': 'Node added successfully'}, status=status.HTTP_200_OK)



    return GenericTreeViewSet

def customTreeNodeViewSet(serializer_class, model):
    class GenericTreeNodeViewSet(viewsets.ModelViewSet):
        queryset = model.objects.all()

        def get_serializer_class(self):
            return serializer_class

        @action(detail=True, methods=['post'])
        def add_child(self, request, pk=None):
            parent_node = self.get_object()
            child_data = request.data
            child_serializer = self.get_serializer(data=child_data)

            if child_serializer.is_valid():
                child_node = child_serializer.save()
                parent_node.add_child(child_node)
                return Response(child_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(child_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @action(detail=True, methods=['post'])
        def associate_node(self, request, pk=None):
            # Get the current node
            current_node = self.get_object()

            # Retrieve the ID of the node to associate
            target_node_id = request.data.get('id')
            if not target_node_id:
                return Response({'error': 'Node ID is required'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                # Fetch the node to be associated
                target_node = TreeNode.objects.get(pk=target_node_id)
            except model.DoesNotExist:
                return Response({'error': 'TreeNode with the given ID does not exist.'}, status=status.HTTP_404_NOT_FOUND)

            # Associate the target node with the current node
            current_node.associate_node(target_node)

            return Response({'status': 'Node associated successfully'}, status=status.HTTP_200_OK)

    return GenericTreeNodeViewSet
