# ruff: noqa
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from network.views import MapViewSet, NetworkViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"network", NetworkViewSet, basename="network")
router.register(r"map", MapViewSet, basename="map")

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("__reload__/", include("django_browser_reload.urls")),
    path("api/", include(router.urls)),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    path(
        "network/",
        TemplateView.as_view(template_name="pages/network.html"),
        name="network",
    ),
    path("map/", TemplateView.as_view(template_name="pages/map.html"), name="map"),
    # Django Admin, use {% url 'admin:index' %}
    path("taggit/", include("taggit_selectize.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("sagebrush.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
