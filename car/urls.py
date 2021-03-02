from django.urls import path
from .views import CarCreateView

urlpatterns = [
    path('sell/', CarCreateView.as_view(), name='sell'),
]