from django.utils.translation import get_language
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly


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
        category = self.request.GET.get("category")
        author = self.request.GET.get("author")
        search = self.request.GET.get("search")  # اضافه کردن جستجو
        if category:
            queryset = queryset.filter(category__icontains=category)
        if author:
            queryset = queryset.filter(author__username__icontains=author)
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_language'] = get_language()  # زبان جاری
        context['total_posts'] = BlogPost.objects.count()  # تعداد کل مقالات
        return context


# جزئیات مقاله
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blogpost_detail.html"
    context_object_name = "blog_post"

    def get_object(self, queryset=None):
        slug = self.kwargs.get("slug")
        return get_object_or_404(BlogPost, slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_language'] = get_language()  # زبان جاری را اضافه می‌کنیم
        return context


# لیست مقالات
class BlogPostListAPI(ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        queryset = BlogPost.objects.all().order_by("-published_date")
        category = self.request.query_params.get("category")
        author = self.request.query_params.get("author")
        if category:
            queryset = queryset.filter(category__icontains=category)
        if author:
            queryset = queryset.filter(author__username__icontains=author)
        return queryset


# جزئیات مقاله
class BlogPostDetailAPI(RetrieveAPIView):
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    queryset = BlogPost.objects.all()


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-published_date')  # لیست مقالات مرتب‌شده بر اساس تاریخ انتشار
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # کاربران غیرمجاز فقط می‌توانند مقالات را مشاهده کنند

    def perform_create(self, serializer):
        # تنظیم نویسنده به کاربر جاری هنگام ایجاد مقاله
        serializer.save(author=self.request.user)




