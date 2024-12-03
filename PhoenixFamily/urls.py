from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from Blog.sitemap import BlogPostSitemap

sitemaps = {
    'blog': BlogPostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),  # مسیر پنل ادمین
    path('set_language/', include('django.conf.urls.i18n')),  # مسیر تغییر زبان
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),

]

urlpatterns += i18n_patterns(
    path('', include('Home.urls', namespace='home')),  # مسیر URLهای اپلیکیشن Home
    path('about/', include('About.urls', namespace='about')),  # مسیر URLهای اپلیکیشن About
    path('blogs/', include('Blog.urls', namespace='blogs')),  # مسیر URLهای اپلیکیشن Blog
    path('contact/', include('Contact.urls', namespace='contact')),  # مسیر URLهای اپلیکیشن Contact
    path('home/', include('Home.urls', namespace='home')),  # مسیر URLهای اپلیکیشن Home
    path('products/', include('Product.urls', namespace='products')),  # مسیر URLهای اپلیکیشن Product
)
