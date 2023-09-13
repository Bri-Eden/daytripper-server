"""View module for handling requests about activity types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daytripperapi.models import ActivityType


class ActivityTypeView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type"""
        activity_type = ActivityType.objects.get(pk=pk)
        serializer = ActivityTypeSerializer(activity_type)

        """Returns:
            Response -- JSON serialized game type
        """
        return Response(serializer.data)
    

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        activity_types = ActivityType.objects.all()
        serializer = ActivityTypeSerializer(activity_types, many=True)
        return Response(serializer.data)


class ActivityTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = ActivityType
        fields = ('id', 'type', 'activity')