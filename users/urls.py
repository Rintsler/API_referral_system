from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDelete, SendConfirmationCode, VerifyConfirmationCode

urlpatterns = [
    path('users', UserListCreate.as_view(), name="Create-User-List"),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name="user-Details"),
    path('send_confirmation_code/', SendConfirmationCode.as_view(), name='send_confirmation_code'),
    path('verify_confirmation_code/', VerifyConfirmationCode.as_view(), name='verify_confirmation_code'),
]
