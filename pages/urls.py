from django.urls import path
from .views import HomePageView, AboutPageView

#  CreatePageView, DetailPageView, EditPageView, ListPageView

urlpatterns = [
    path("home/", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
#     path("create/", CreatePageView.as_view(), name="create"),
#     path("detail/", DetailPageView.as_view(), name="detail"),
#     path("edit/", EditPageView.as_view(), name="edit"),
#     path("list/", ListPageView.as_view(), name="list"),
# ]