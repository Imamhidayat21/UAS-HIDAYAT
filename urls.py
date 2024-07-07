from django.urls import path
from . import views

urlpatterns = [
    path("blogpost/", views.BlogpostlistCreate.as_view(), name="blogpost-view-create"),
    path("blogpost/<int:pk>/", views.BlogPostRetrieveUpdateDestory.as_view(), name="update",),
]