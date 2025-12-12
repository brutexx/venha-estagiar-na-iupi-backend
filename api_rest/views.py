from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    # 1. Define a fonte de informação
    queryset = Transaction.objects.all()
    # 2. Define como converter a informação
    serializer_class = TransactionSerializer