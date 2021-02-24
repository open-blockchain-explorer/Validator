from rest_framework.routers import SimpleRouter

from .views.transaction_log import TransactionLogViewSet, TransactionLogDetailViewSet

router = SimpleRouter(trailing_slash=False)
router.register('transactions', TransactionLogViewSet)
router.register('transactions', TransactionLogDetailViewSet, basename='transaction_detail')
