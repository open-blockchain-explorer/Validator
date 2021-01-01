from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics

from v1.cache_tools.accounts import get_account_balance, get_account_balance_lock
from ..models.transaction_log import TransactionLog
from ..serializers.transaction_log import TransactionLogSerializer, TransactionLogDetailSerializer


class TransactionLogViewSet( 
    ListModelMixin,
    GenericViewSet,
):
    """
    Transaction Log List View

    Description: List all the transaction
    """

    ordering_fields = '__all__'
    queryset = TransactionLog.objects.all()
    serializer_class = TransactionLogSerializer

class TransactionLogDetailViewSet(
  generics.RetrieveAPIView,
  GenericViewSet
  ):
  """
    Transaction Log Detail View
  
    Description: Get the details of a particular transaction
  """
  queryset = TransactionLog.objects.all()
  serializer_class = TransactionLogDetailSerializer