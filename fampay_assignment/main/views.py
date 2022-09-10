import time
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import FetchedYoutubeDataSerializer
from main.models import FetchedYoutubeData
from main.pagination import SimpleDataPagination
from rest_framework.viewsets import ViewSet
from main.service import YoutubeDataService
from rest_framework import status as resp_status
# Create your views here.


@api_view(["GET"])
def test_api_view(request):

    if request.method == "GET":
        return Response({"data": None})


class YoutubeDataSearchViewset(ViewSet):
    """
    search api for fetched data
    """
    pagination_class = SimpleDataPagination()

    def search(self, request):

        search_title = request.query_params.get("title")
        search_description = request.query_params.get("description")

        status, data = YoutubeDataService.search_youtube_data(
            search_description=search_description, search_title=search_title)

        if not status:
            return Response(data={"error": data}, status=resp_status.HTTP_404_NOT_FOUND)

        paginated_queryset = self.pagination_class.paginate_queryset(data,request)
        serialized_data = FetchedYoutubeDataSerializer(
            paginated_queryset, many=True).data

        return self.pagination_class.get_paginated_response(serialized_data)


class YoutubeDataListViewset(ViewSet):
    """
    list api for fetched data
    """
    pagination_class = SimpleDataPagination()

    def list(self, request):

        all_data = FetchedYoutubeData.objects.all().order_by("-published_on")

        if not all_data:
            return Response(data={"error": "No data found"}, status=resp_status.HTTP_404_NOT_FOUND)

        paginated_queryset = self.pagination_class.paginate_queryset(
            all_data, request)

        serialized_data = FetchedYoutubeDataSerializer(
            paginated_queryset, many=True).data

        return self.pagination_class.get_paginated_response(serialized_data)
