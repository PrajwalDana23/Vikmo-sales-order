from rest_framework.viewsets import ModelViewSet
from .models import Dealer
from .serializers import DealerSerializer

class DealerViewSet(ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer