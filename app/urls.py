from django.urls import path
from app import views


urlpatterns = [
    path('', views.OrderListView.as_view(), name='orders'),
]