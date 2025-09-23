from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_feedback_view, name='product_feedback'),
]
