from django.urls import path

from app.views import (
    TagListView,
    TagUpdateView,
    TagCreateView,
    TagDeleteView,
    TaskListView,
    TaskUpdateView,
    TaskDeleteView,
    task_status,
    TaskCreateView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "task/<int:pk>/task-status/",
        task_status,
        name="task-status",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
]

app_name = "app"
