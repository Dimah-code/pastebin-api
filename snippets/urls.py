from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    SnippetDetail,
    SnippetList,
    SnippetHighlight,
    UserDetail,
    UserList,
    api_root,
)

urlpatterns = format_suffix_patterns(
    [
        # Root
        path("", api_root),
        # Snippets
        path("snippets/", SnippetList.as_view(), name="snippet-list"),
        path("snippets/<int:pk>/", SnippetDetail.as_view(), name="snippet-detail"),
        path(
            "snippets/<int:pk>/highlight/",
            SnippetHighlight.as_view(),
            name="snippet-highlight",
        ),
        # Users
        path("users/", UserList.as_view(), name="user-list"),
        path("user/<int:pk>/", UserDetail.as_view(), name="user-detail"),
    ]
)
