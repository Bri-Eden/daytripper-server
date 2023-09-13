"""View module for handling requests about planners"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daytripperapi.models import Planner


class PlannerView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single planner"""
        planner = Planner.objects.get(pk=pk)
        serializer = PlannerSerializer(planner)

        """Returns:
            Response -- JSON serialized game type
        """
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        planners = Planner.objects.all()
        serializer = PlannerSerializer(planners, many=True)
        return Response(serializer.data)


class PlannerSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Planner
        fields = ('id', 'location', 'photo', 'trip')
