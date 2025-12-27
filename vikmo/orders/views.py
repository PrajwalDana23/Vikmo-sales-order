from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from inventory.models import Inventory
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        order = self.get_object()

        if order.status != 'DRAFT':
            return Response(
                {"error": "Invalid status"},
                status=400
            )

        with transaction.atomic():
            # Lock inventory rows
            for item in order.items.all():
                inv = Inventory.objects.select_for_update().get(
                    product=item.product
                )

                if item.quantity > inv.quantity:
                    return Response(
                        {
                            "error": f"Insufficient stock for {item.product.name}",
                            "available": inv.quantity,
                            "requested": item.quantity
                        },
                        status=400
                    )

            # Deduct inventory
            for item in order.items.all():
                inv = Inventory.objects.select_for_update().get(
                    product=item.product
                )
                inv.quantity -= item.quantity
                inv.save()

            order.status = 'CONFIRMED'
            order.save()

        return Response({"message": "Order confirmed"})

    @action(detail=True, methods=['post'])
    def deliver(self, request, pk=None):
        order = self.get_object()

        if order.status != 'CONFIRMED':
            return Response(
                {"error": "Invalid status"},
                status=400
            )

        order.status = 'DELIVERED'
        order.save()

        return Response({"message": "Order delivered"})