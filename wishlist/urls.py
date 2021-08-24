from django.urls import path

from .views import AddItemView, GetItemsView, GetItemTotalView, RemoveItemView

urlpatterns = [
    path('wishlist-items', GetItemsView.as_view()),
    path('add-item', AddItemView.as_view()),
    path('get-item-total', GetItemTotalView.as_view()),
    path('remove-item', RemoveItemView.as_view()),
]
