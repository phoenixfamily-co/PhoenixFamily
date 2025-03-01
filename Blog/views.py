from django.db.models import Q
from django.utils.timezone import now
from django.utils.translation import get_language
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.utils.translation import gettext_lazy as _

from About.models import AboutUs
from Blog.models import BlogPost
from Blog.serializers import BlogPostSerializer


# لیست مقالات
class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blogs.html"
    context_object_name = "blog_posts"
    paginate_by = 10  # تعداد مقالات در هر صفحه

    def get_queryset(self):
        queryset = BlogPost.objects.all().order_by("-published_date")
        filters = Q()
        category = self.request.GET.get("category")
        author = self.request.GET.get("author")
        search = self.request.GET.get("search")

        if category:
            filters &= Q(category__iexact=category)
        if author:
            filters &= Q(author__username__icontains=author)
        if search:
            filters &= Q(title__icontains=search)

        return queryset.filter(filters)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = BlogPost.objects.count()  # تعداد کل مقالات
        context['About'] = AboutUs.objects.first()

        return context

    def get_page_description(self):
        # اینجا می‌توانید توصیف صفحه را بر اساس مدل یا داده‌های دیگر بسازید
        return _("Discover Insights, Stories, and Innovations.")

    def get_page_keywords(self):
        # اینجا می‌توانید کلمات کلیدی را بر اساس مدل یا داده‌های دیگر بسازید
        return _("phoenixfamily, blog, post, article, Insights, Stories, Innovations ")

    def get_page_title(self):
        return _("blogs")  # عنوان صفحه بر اساس زبان انتخابی

    def get_page_date_published(self):
        # برای صفحات جستجو یا دسته‌بندی می‌توانید از تاریخ فعلی استفاده کنید
        return now().strftime('%Y-%m-%dT%H:%M:%S+00:00')


# جزئیات مقاله
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blogpost.html"
    context_object_name = "blog_post"

    def get_object(self, queryset=None):
        slug = self.kwargs.get("slug")
        return get_object_or_404(BlogPost, slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_language'] = get_language()  # زبان جاری را اضافه می‌کنیم

        page_title = self.get_page_title()  # عنوان صفحه
        page_description = self.get_page_description()  # توصیف صفحه
        page_keywords = self.get_page_keywords()  # کلمات کلیدی
        canonical_url = self.request.build_absolute_uri(self.request.path)

        context['page_title'] = page_title
        context['page_description'] = page_description
        context['page_keywords'] = page_keywords
        context['canonical_url'] = canonical_url

        return context

    def get_page_title(self):
        # شما می‌توانید عنوان صفحه را بر اساس عنوان مقاله بسازید
        blog_post = self.get_object()
        return blog_post.meta_title

    def get_page_description(self):
        # توصیف صفحه می‌تواند از محتوای مقاله گرفته شود
        blog_post = self.get_object()
        return blog_post.meta_description  # یا هر فیلدی که توصیف کوتاهی از مقاله باشد

    def get_page_keywords(self):
        # کلمات کلیدی می‌تواند بر اساس دسته‌بندی یا برچسب‌های مقاله باشد
        blog_post = self.get_object()
        return blog_post.meta_keywords  # اگر مقاله دسته‌بندی‌ها داشته باشد


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-published_date')  # لیست مقالات مرتب‌شده بر اساس تاریخ انتشار
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # کاربران غیرمجاز فقط می‌توانند مقالات را مشاهده کنند

    def perform_create(self, serializer):
        # تنظیم نویسنده به کاربر جاری هنگام ایجاد مقاله
        serializer.save(author=self.request.user)
