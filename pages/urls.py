from django.urls import path
from . import views  # 현재 디렉토리에서부터 views 를 가져옴

# domain.com/pages/____
urlpatterns = [
    path('greeting/<str:name>/', views.greeting),
    path('', views.index),
]
