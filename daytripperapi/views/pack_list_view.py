"""View module for handling requests about trips"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daytripperapi.models import Trip, PackItem, PackList


class PackListView(ViewSet):
    """trip views"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trip"""
        packlist = PackList.objects.get(pk=pk)
        serializer = PacklistSerializer(packlist)

        """Returns:
            Response -- JSON serialized trip
        """
        return Response(serializer.data)

    def list(self, request, pk):
        """Handle GET requests for single trip"""
        packlists = PackList.objects.filter(pk=pk)
        if not packlists.exists():
            return Response(
                {"error": "PackList not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PacklistSerializer(packlists.first())
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized pack item instance
        """
        packitem = PackItem.objects.get(
            pk=request.data["packitem"])

        trip = Trip.objects.get(
            pk=request.data["trip"])

        packlist = PackList.objects.create(
            packitem=packitem,
            trip=trip
        )
        serializer = PackItemSerializer(packitem)
        return Response(serializer.data)


class PackItemSerializer(serializers.ModelSerializer):
    """JSON serializer for trip types
    """
    class Meta:
        model = PackItem
        fields = ('id', 'planner', 'item_type', 'item_name',
                  'amount', 'description')


class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for trip types
    """
    class Meta:
        model = Trip
        fields = ('id', 'planner', 'destination',
                  'num_of_days', 'num_of_nights', 'climate')


class PacklistSerializer(serializers.ModelSerializer):
    """JSON serializer for trip types
    """
    packitem = PackItemSerializer(many=False)
    trip = TripSerializer(many=False)

    class Meta:
        model = PackList
        fields = ('id', 'packitem', 'trip')
