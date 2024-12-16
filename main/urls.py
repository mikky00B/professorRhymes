from django.urls import path
from . import views
from .views import (
    BlogListView,
    BlogDetailView,
    blog_detail,
    blog_list,
    home,
    about,
    portfolio,
    contact,
)


app_name = "blog"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact", contact, name="contact"),
    path("portfolio/", portfolio, name="works"),
    path("blog/", BlogListView.as_view(), name="blog"),
    path(
        "blog/category/<slug:category_slug>/",
        BlogListView.as_view(),
        name="blog_by_category",
    ),
    path("blog/tag/<slug:tag_slug>/", BlogListView.as_view(), name="blog_by_tag"),
    path("blog/<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
]

## function based

# urlpatterns = [
#     path('blog/', blog_list, name='blog_list'),
#     path('blog/category/<slug:category_slug>/', blog_list, name='blog_by_category'),
#     path('blog/tag/<slug:tag_slug>/', blog_list, name='blog_by_tag'),
#     path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
# ]
