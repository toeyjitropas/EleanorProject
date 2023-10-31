from django.urls import path
from .views import get_transaction

urlpatterns = [
    path('v1/<int:id>', get_transaction),
]