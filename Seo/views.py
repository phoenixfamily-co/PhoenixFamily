from rest_framework import viewsets

from Seo.models import SEOPage, Keyword
from Seo.serializers import SEOPageSerializer, KeyWordSerializer


class SEOPageView(viewsets.ModelViewSet):
    queryset = SEOPage.objects.all()
    serializer_class = SEOPageSerializer


class KeywordView(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeyWordSerializer

