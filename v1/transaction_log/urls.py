from rest_framework.routers import SimpleRouter

from .views.transaction_log import TransactionLogViewSet

router = SimpleRouter(trailing_slash=False)
router.register('transactions', TransactionLogViewSet)
