from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet

# Cria um roteador (gera as URLS por conta própria)
router = DefaultRouter()
# Registra o meu ViewSet nele
router.register(r'', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]