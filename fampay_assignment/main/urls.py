from urllib import request
from django.urls import path
from main.views import test_api_view, YoutubeDataListViewset, YoutubeDataSearchViewset

urlpatterns = [
    path('', test_api_view, name="test_view"),

    path('list/', YoutubeDataListViewset.as_view({"get":"list"}), name="list_fetched_youtube_data"),

    path('search/', YoutubeDataSearchViewset.as_view({"get":"search"}), name="search_fetched_youtube_data"),
]