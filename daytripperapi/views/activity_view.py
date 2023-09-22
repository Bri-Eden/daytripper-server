"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daytripperapi.models import Trip, Activity, ActivityType, Planner


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
        trip = self.request.query_params.get('trip')

        if trip is not None:
            activity = Activity.objects.filter(trip=trip)
        else:
            activity = Activity.objects.all()

        serialized = ActivitySerializer(activity, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request, pk):
        """Handle POST operations

        Returns
        Response -- JSON serialized game instance
        """
        # would this be user? or planner?
        trip = Trip.objects.get(pk=pk)
        activity_type = ActivityType.objects.get(
            pk=request.data["activity_type"])

        activity = Activity.objects.create(
            title=request.data["title"],
            day=request.data["day"],
            time=request.data["time"],
            description=request.data["description"],
            trip=trip,
            activity_type=activity_type
        )
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a activity

        Returns:
        Response -- Empty body with 204 status code
            """
        trip = Trip.objects.get(pk=pk)
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


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ('id', 'planner',
                  'destination', 'arrival', 'departure')


class ActivityTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = ActivityType
        fields = ('id', 'type')


class ActivitySerializer(serializers.ModelSerializer):
    """JSON serializer for trip types
    """
    activity_type = ActivityTypeSerializer(many=False)
    trip = TripSerializer(many=False)

    class Meta:
        model = Activity
        fields = ('id', 'trip', 'activity_type', 'title',
                  'day', 'time', 'description')
