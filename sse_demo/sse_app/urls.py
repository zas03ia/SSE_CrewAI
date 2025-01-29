from django.urls import path
from . import views

urlpatterns = [
    path('sse/', views.sse_view),  # SSE view endpoint
]
