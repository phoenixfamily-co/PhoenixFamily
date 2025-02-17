from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from Blog.sitemap import *
from PhoenixFamily import settings
from django.conf.urls.i18n import set_language


sitemaps = {
    'blog_list': BlogPostListSitemap,
    'blog_details': BlogPostDetailSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),  # مسیر پنل ادمین
    path('set_language/', set_language, name='set_language'),  # به جای include از set_language استفاده کنید
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),

]

urlpatterns += i18n_patterns(
    path('about/', include('About.urls', namespace='about')),  # مسیر URLهای اپلیکیشن About
    path('blogs/', include('Blog.urls', namespace='blogs')),  # مسیر URLهای اپلیکیشن Blog
    path('contact/', include('Contact.urls', namespace='contact')),  # مسیر URLهای اپلیکیشن Contact
    path('home/', include('Home.urls', namespace='home')),  # مسیر URLهای اپلیکیشن Home
    path('products/', include('Product.urls', namespace='products')),  # مسیر URLهای اپلیکیشن Product
    path('user/', include('User.urls', namespace='user')),  # مسیر URLهای اپلیکیشن User
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
