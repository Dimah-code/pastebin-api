from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import snippet_detail, snippet_list

urlpatterns = [
    path("snippets/", snippet_list),
    path("snippets/<int:pk>/", snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
