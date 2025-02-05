from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    get_or_create_temporary_user,
    log_user_activity,
    log_exit_time,
    UserCRUDView,
)

app_name = "user"

# Create a router for the UserCRUDView (ModelViewSet)
router = DefaultRouter()
router.register(r'user-CRUD', UserCRUDView, basename='user')

urlpatterns = [
    # Function-based views
    path('api/create-temporary-user/', get_or_create_temporary_user, name='create_temporary_user'),
    path('api/log-activity/', log_user_activity, name='log_activity'),
    path('api/log-exit-time/', log_exit_time, name='log_exit_time'),

    # Include the router URLs for UserCRUDView
    path('api/', include(router.urls)),
]