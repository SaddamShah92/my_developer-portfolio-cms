from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, BlogSitemap

def robots_txt(request):
    content = """User-agent: *
Allow: /

Disallow: /admin/

Sitemap: /sitemap.xml
"""

    return HttpResponse(
        content,
        content_type="text/plain"
    )

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('services/', views.services, name = 'services'),
    path('projects/', views.projects, name = 'projects'),
    path('resume/', views.resume , name = 'resume'),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("robots.txt",robots_txt,name="robots"),
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps}, name="sitemap"),
]


# MEDIA FILES CONFIG

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


