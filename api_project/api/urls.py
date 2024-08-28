
# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()  # Instantiate a default router
router.register(r'books', BookViewSet)  # Register the BookViewSet with the router

urlpatterns = [
    path('', include(router.urls)),  # Include the router-generated URL patterns
]
