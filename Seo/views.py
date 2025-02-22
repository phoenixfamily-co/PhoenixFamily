from rest_framework import viewsets

from Seo.models import SEOPage
from Seo.serializers import SEOPageSerializer


class SEOPageView(viewsets.ModelViewSet):
    queryset = SEOPage.objects.all()
    serializer_class = SEOPageSerializer


