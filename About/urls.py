from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsCRUDView, FAQCRUDView, about


app_name = 'about'

router = DefaultRouter()
router.register(r'about-info', UsCRUDView)
router.register(r'FAQ-info', FAQCRUDView)


urlpatterns = [
    path('', about, name='about-view'),  # صفحه اصلی
    path('api/', include(router.urls)),
]
