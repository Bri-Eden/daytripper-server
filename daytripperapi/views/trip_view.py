"""View module for handling requests about trips"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daytripperapi.models import Trip, Planner, TransportationType


class TripView(ViewSet):
    """trip views"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trip"""
        trip = Trip.objects.get(pk=pk)
        serializer = TripSerializer(trip)

        """Returns:
            Response -- JSON serialized trip
        """
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to posts resource
        Returns:
            Response -- JSON serialized list of trips
        """
        trips = Trip.objects.order_by('arrival')
        if "current" in request.query_params:
            planner = Planner.objects.get(user=request.auth.user.id)
            trips = trips.filter(planner=planner)

        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized game instance
        """
        planner = Planner.objects.get(user=request.auth.user)
        mode_of_transport = TransportationType.objects.get(pk=request.data["mode_of_transport"])

        trip = Trip.objects.create(
            cover_photo=request.data["cover_photo"],
            destination=request.data["destination"],
            num_of_days=request.data["num_of_days"],
            num_of_nights=request.data["num_of_nights"],
            climate=request.data["climate"],
            arrival=request.data["arrival"],
            departure=request.data["departure"],
            planner=planner,
            mode_of_transport=mode_of_transport
        )
        serializer = TripSerializer(trip)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a trip

        Returns:
        Response -- Empty body with 204 status code
            """
      # planner = Planner.objects.get(pk=request.data["id"])
      # planner = Planner.objects.get(user=request.auth.user.id)
        mode_of_transport = TransportationType.objects.get(
            pk=request.data["mode_of_transport"])
        
        trip = Trip.objects.get(pk=pk)

        trip.cover_photo = request.data["cover_photo"]
        trip.destination = request.data["destination"]
        trip.num_of_days = request.data["num_of_days"]
        trip.num_of_nights = request.data["num_of_nights"]
        trip.climate = request.data["climate"]
        trip.arrival = request.data["arrival"]
        trip.departure = request.data["departure"]
        trip.mode_of_transport = mode_of_transport

        trip.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        trip.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for trip types
    """
    class Meta:
        model = Trip
        fields = ('id', 'planner', 'mode_of_transport', 'cover_photo',
                  'destination', 'num_of_days', 'num_of_nights', 'climate',
                  'arrival', 'departure', 'activities')
