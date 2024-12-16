from django import forms
from tinymce.widgets import TinyMCE
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30}))

    class Meta:
        model = BlogPost
        fields = [
            "title",
            "content",
            "category",
            "tags",
            "featured_image",
            "published",
            "meta_description",
            "meta_keywords",
        ]
