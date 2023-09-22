"""View module for handling requests about planners"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daytripperapi.models import Planner
from rest_framework.authtoken.models import Token


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

        token = request.query_params.get("token", None)
        if token:
            user = Token.objects.get(key=token).user
            planners = Planner.objects.get(user=user)

        serializer = PlannerSerializer(planners)
        return Response(serializer.data)


class PlannerSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Planner
        fields = ('id', 'user', 'full_name', 'location', 'photo', 'trip')
