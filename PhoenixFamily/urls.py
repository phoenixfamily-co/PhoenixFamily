from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # مسیر پنل ادمین
    path('set_language/', include('django.conf.urls.i18n')),  # مسیر تغییر زبان
]

urlpatterns += i18n_patterns(
    path('', include('About.urls', namespace='about')),  # مسیر URLهای اپلیکیشن About
    path('', include('Blog.urls', namespace='blogs')),  # مسیر URLهای اپلیکیشن Blog
    path('', include('Contact.urls', namespace='contact')),  # مسیر URLهای اپلیکیشن Contact
    path('', include('Home.urls'), namespace='home'),  # مسیر URLهای اپلیکیشن Home
    path('', include('Product.urls', namespace='products')),  # مسیر URLهای اپلیکیشن Product
    path('', include('User.urls', namespace='user')),  # مسیر URLهای اپلیکیشن User
)
