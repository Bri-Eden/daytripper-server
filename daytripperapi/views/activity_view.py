"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daytripperapi.models import Trip, Activity, ActivityType


class ActivityView(ViewSet):
    """trip views"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trip"""
        activity = Activity.objects.get(pk=pk)
        serializer = ActivitySerializer(activity)

        """Returns:
            Response -- JSON serialized trip
        """
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to posts resource
        Returns:
            Response -- JSON serialized list of trips
        """
        activities = Activity.objects.order_by('day')
        if "user" in request.query_params:
            trip = Trip.objects.get(user=request.auth.user)
            activities = activities.filter(trip=trip)

        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized game instance
        """
        #would this be user? or planner?
        trip = Trip.objects.get(user=request.auth.user)
        activity_type = ActivityType.objects.get(
            pk=request.data["activity_type"])

        trip = Trip.objects.create(
            title=request.data["title"],
            day=request.data["day"],
            time=request.data["time"],
            description=request.data["description"],
            trip=trip,
            activity_type=activity_type
        )
        serializer = ActivitySerializer(trip)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a activity

        Returns:
        Response -- Empty body with 204 status code
            """
        trip = Trip.objects.get(user=request.auth.user)
        activity_type = ActivityType.objects.get(
            pk=request.data["activity_type"])

        activity = Activity.objects.get(pk=request.data["activity"])

        activity.title = request.data["cover_photo"],
        activity.day = request.data["destination"],
        activity.time = request.data["num_of_days"],
        activity.description = request.data["num_of_nights"],
        activity.trip = trip,
        activity.activity_type = activity_type

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ActivitySerializer(serializers.ModelSerializer):
    """JSON serializer for trip types
    """
    class Meta:
        model = Activity
        fields = ('id', 'trip', 'activity_type', 'title',
                  'day', 'time', 'description', 'activity')
