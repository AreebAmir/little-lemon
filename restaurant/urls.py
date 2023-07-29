from django.urls import path, include
from .views import index, menuView, bookingView

urlpatterns = [
    path('', index, name='index'),
    path('/booking', bookingView.as_view()),
    path('/menu', menuView.as_view())
]