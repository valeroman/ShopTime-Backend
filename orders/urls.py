from django.urls import path

from .views import CreateOrderView, ListOrderDetailView, ListOrdersView

urlpatterns = [
    path('get-orders', ListOrdersView.as_view()),
    path('get-order/<transactionId>', ListOrderDetailView.as_view()),
    path('create-order', CreateOrderView.as_view()),
]
