from django.urls import path
from .views import CreateTicketView, UploadImageView, TicketListView, TicketDetailView

urlpatterns = [
    path('create/', CreateTicketView.as_view(), name='create-ticket'),
    path('upload/', UploadImageView.as_view(), name='upload-image'),
    path('list/', TicketListView.as_view(), name='list-tickets'),
    path('detail/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
]
