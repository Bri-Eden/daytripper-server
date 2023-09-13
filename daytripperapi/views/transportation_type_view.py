"""View module for handling requests about trabspo"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daytripperapi.models import TransportationType


class TransportaionTypeView(ViewSet):
    """Level up transportation types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single transportation type"""
        transportation_type = TransportationType.objects.get(pk=pk)
        serializer = TransportationTypeSerializer(transportation_type)

        """Returns:
            Response -- JSON serialized type
        """
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all transpo types

        Returns:
            Response -- JSON serialized list of types
        """
        transportation_types = TransportationType.objects.all()
        serializer = TransportationTypeSerializer(transportation_types, many=True)
        return Response(serializer.data)


class TransportationTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for transpo types
    """
    class Meta:
        model = TransportationType
        fields = ('id', 'type')
