"""
Django settings for careerSite project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-i4)q92+d1cq81u31y(!hmo+9jpa($m6x76fl00wgq%$wpcraf_"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
    "tinymce",
    "grappelli",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "careerSite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "careerSite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TINYMCE_DEFAULT_CONFIG = {
    "height": 500,  # Editor height in pixels
    "width": "100%",  # Set the width of the editor
    "plugins": """
        autolink autosave code link lists image charmap preview hr
        anchor pagebreak searchreplace wordcount visualblocks
        visualchars insertdatetime media nonbreaking table
        emoticons template paste help codemirror spellchecker imagetools
        fullscreen advlist advcode advtable toc
        textcolor colorpicker textpattern imagetools
        contextmenu
    """,  # List of plugins to enable (added advlist, advcode, advtable, etc.)
    "toolbar": """
        undo redo | formatselect | fontselect fontsizeselect | bold italic underline strikethrough | 
        alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | 
        link image media table | forecolor backcolor | fullscreen code preview | 
        emoticons charmap hr anchor pagebreak | removeformat | spellchecker
    """,  # Enhanced toolbar with font and text controls
    "menu": {
        "file": {
            "title": "File",
            "items": "newdocument restoredraft | preview | print",
        },
        "edit": {"title": "Edit", "items": "undo redo | cut copy paste | selectall"},
        "view": {"title": "View", "items": "visualaid | fullscreen"},
        "insert": {"title": "Insert", "items": "image link media template hr toc"},
        "format": {
            "title": "Format",
            "items": "bold italic underline strikethrough superscript subscript | formats blockformats fontformats align | removeformat",
        },
        "tools": {"title": "Tools", "items": "spellchecker code"},
        "table": {
            "title": "Table",
            "items": "inserttable | cell row column | deletetable",
        },
    },
    "menubar": True,  # Show the menubar
    "statusbar": True,  # Enable the status bar at the bottom
    "branding": False,  # Disable "Powered by TinyMCE" branding
    "elementpath": False,  # Hide the path in the status bar
    "content_css": "/static/css/custom_content_styles.css",  # Custom content styles
    # "file_picker_callback": 'function (callback, value, meta) { console.log("file picker triggered"); }',  # File picker for images/media
    "automatic_uploads": True,  # Automatically upload images
    "image_advtab": True,  # Show advanced tab when editing images
    "relative_urls": False,  # Avoid issues with media paths
    "media_live_embeds": True,  # Allow media embedding like YouTube
    "image_caption": True,  # Allow adding captions to images
    "image_advtab": True,
    "file_picker_types": "file image media",  # File picker types
    "file_browser_callback_types": "file image media",  # File browser callback types
    # "file_picker_callback": 'function(callback, value, meta) {window.open("/admin/filebrowser/browse/?pop=3", "FileBrowser", "width=800,height=600");}',
    "fontsize_formats": "8pt 10pt 12pt 14pt 18pt 24pt 36pt 48pt",  # Font size options
    "font_formats": "Arial=arial,helvetica,sans-serif; Courier New=courier new,courier,monospace; Georgia=georgia,palatino; Times New Roman=times new roman,times; Verdana=verdana,geneva;",
    "textpattern_patterns": [  # Custom text patterns for shortcuts
        {"start": "*", "end": "*", "format": "italic"},
        {"start": "**", "end": "**", "format": "bold"},
        {"start": "#", "format": "h1"},
        {"start": "##", "format": "h2"},
        {"start": "###", "format": "h3"},
    ],
}
