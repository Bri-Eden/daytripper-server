"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daytripperapi.models import ItemType


class ItemTypeView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type"""
        item_type = ItemType.objects.get(pk=pk)
        serializer = ItemTypeSerializer(item_type)

        """Returns:
            Response -- JSON serialized game type
        """
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        item_types = ItemType.objects.all()
        serializer = ItemTypeSerializer(item_types, many=True)
        return Response(serializer.data)


class ItemTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = ItemType
        fields = ('id', 'type')
