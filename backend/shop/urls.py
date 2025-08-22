from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('all', ProductListView.as_view()),
    path('<int:product_id>', ProductDetailView.as_view())
]