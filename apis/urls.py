from django.urls import path

from books import urls

from .views import BookListView

urlpatterns = [
    path("", BookListView.as_view(), name="home"),
]