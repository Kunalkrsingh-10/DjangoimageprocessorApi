
from django.urls import path
from . import views

urlpatterns = [
    path('upload_csv/', views.upload_csv),
    path('status/<str:request_id>/', views.check_status),
]
