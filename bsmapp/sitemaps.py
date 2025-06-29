from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog, Service

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        # Sadece anasayfa
        return ['bsmapp:index']

    def location(self, item):
        return reverse(item)

class ServiceSitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'

    def items(self):
        return Service.objects.all()

    def location(self, obj):
        return reverse('bsmapp:service_detail', args=[obj.pk])

class AboutSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['bsmapp:about']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return reverse('bsmapp:blog_single', args=[obj.pk])

    def lastmod(self, obj):
        return obj.date 