from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # مسیر پنل ادمین
    path('set_language/', include('django.conf.urls.i18n')),  # مسیر تغییر زبان
]

urlpatterns += i18n_patterns(
    path('', include('Home.urls')),  # مسیر URLهای اپلیکیشن Home
)
