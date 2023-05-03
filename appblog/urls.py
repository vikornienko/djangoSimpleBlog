from django.urls import path

from .views import post_detail, post_share, PostListView

app_name = "appblog"

urlpatterns = [
    # path("", post_list, name="post_list"),
    path("", PostListView.as_view(), name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", post_detail, name="post_detail"),
    path('<int:post_id>/share/', post_share, name="post_share"),
]