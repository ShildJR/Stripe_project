from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('item/<int:id>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('buy/<int:id>/', views.CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
    path('success/', views.success_view, name='success'),
]
