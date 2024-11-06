# backend/textbook_marketplace/marketplace/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('textbooks/', views.TextbookListView.as_view(), name='textbook-list'),
    path('textbook/<int:pk>/', views.TextbookDetailView.as_view(), name='textbook-detail'),
    path('textbook/<int:pk>/image/', views.TextbookImageView.as_view()),
]
