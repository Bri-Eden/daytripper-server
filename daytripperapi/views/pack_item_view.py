"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daytripperapi.models import PackItem, Planner, ItemType


class PackItemView(ViewSet):
    """pack item views"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trip"""
        pack_item = PackItem.objects.get(pk=pk)
        serializer = PackItemSerializer(pack_item)

        """Returns:
            Response -- JSON serialized trip
        """
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to posts resource
        Returns:
            Response -- JSON serialized list of trips
        """
        pack_items = PackItem.objects.get(all)
        if "user" in request.query_params:
            planner = Planner.objects.get(user=request.auth.user)
            pack_item = pack_item.filter(planner=planner)

        serializer = PackItemSerializer(pack_items, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized pack item instance
        """
        planner = Planner.objects.get(user=request.auth.user)
        item_type = ItemType.objects.get(
            pk=request.data["item_type"])

        packitem = PackItem.objects.create(
            item_name=request.data["item_name"],
            amount=request.data["amount"],
            description=request.data["description"],
            planner=planner,
            item_type=item_type
        )
        serializer = PackItemSerializer(packitem)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a activity

        Returns:
        Response -- Empty body with 204 status code
            """
        planner = Planner.objects.get(user=request.auth.user)
        item_type = ItemType.objects.get(
            pk=request.data["item_type"])

        pack_item = PackItem.objects.get(pk=request.data["pack_item"])

        pack_item.item_name = request.data["item_name"],
        pack_item.amount = request.data["amount"],
        pack_item.description = request.data["num_of_nights"],
        pack_item.planner = planner,
        pack_item.item_type = item_type

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class PackItemSerializer(serializers.ModelSerializer):
    """JSON serializer for trip types
    """
    class Meta:
        model = PackItem
        fields = ('id', 'planner', 'item_type', 'item_name',
                  'amount', 'description')
