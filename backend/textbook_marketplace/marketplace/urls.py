# backend/textbook_marketplace/marketplace/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProtectedView, SignupView, CustomTokenObtainPairView, TextbookViewSet, UserViewSet, OrderViewSet, get_user_data


from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register(r'textbooks', TextbookViewSet)
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('textbooks/', views.TextbookListView.as_view(), name='textbook-list'),
    path('textbook/<int:pk>/', views.TextbookDetailView.as_view(), name='textbook-detail'),
    path('textbook/<int:pk>/image/', views.TextbookImageView.as_view()),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('signup/', SignupView.as_view()),
    path('textbooks/create/', TextbookViewSet.as_view({'post': 'create_textbook'}), name='create_textbook'),
    path('users/me/', get_user_data, name='get_user_data'),
]
