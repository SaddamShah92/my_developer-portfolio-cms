from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Blog


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            "home",
            "about",
            "services",
            "projects",
            "resume",
            "blog",
            "contact",
        ]

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Blog.objects.filter(status="published")

    def location(self, obj):
        return reverse("blog_detail", kwargs={"slug": obj.slug})

    def lastmod(self, obj):
        return obj.updated_at