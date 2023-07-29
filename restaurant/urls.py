from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.MenuItemView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view())
]