# Generated by Django 5.1.2 on 2024-10-18 21:52

import django.db.models.deletion
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="AuthorProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bio", models.TextField()),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="author_pictures"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("content", tinymce.models.HTMLField()),
                (
                    "excerpt",
                    models.TextField(
                        help_text="Short description for SEO purposes", max_length=500
                    ),
                ),
                (
                    "featured_image",
                    models.ImageField(blank=True, null=True, upload_to="blog_images/"),
                ),
                ("published", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "meta_description",
                    models.CharField(
                        help_text="For SEO meta tag description", max_length=160
                    ),
                ),
                (
                    "meta_keywords",
                    models.CharField(
                        blank=True,
                        help_text="SEO keywords separated by commas",
                        max_length=255,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main.category",
                    ),
                ),
                ("tags", models.ManyToManyField(blank=True, to="main.tag")),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]