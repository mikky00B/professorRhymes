from django.views.generic import ListView, DetailView
from .models import BlogPost, Category, Tag
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        # Get all published blog posts
        queryset = BlogPost.objects.filter(published=True)

        # Filtering by category if provided
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        # Filtering by tag if provided
        tag_slug = self.kwargs.get("tag_slug")
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)

        # Search functionality
        search_query = self.request.GET.get("q")
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        """
        Add context data like categories to the template context.
        """
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "core/blog_detail.html"
    context_object_name = "post"

    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(BlogPost, slug=slug, published=True)


## function based views


def blog_list(request, category_slug=None, tag_slug=None):
    posts = BlogPost.objects.filter(published=True)

    # Filter by category
    if category_slug:
        posts = posts.filter(category__slug=category_slug)

    # Filter by tag
    if tag_slug:
        posts = posts.filter(tags__slug=tag_slug)

    # Search functionality
    search_query = request.GET.get("q")
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )

    # Pagination
    page = request.GET.get("page", 1)
    paginator = Paginator(posts, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog.html", {"posts": posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, "single.html", {"post": post})


def home(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def portfolio(request):
    return render(request, "service.html")


def about(request):
    return render(request, "about.html")
