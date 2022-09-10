from main.models import FetchedYoutubeData
from django.contrib.postgres.search import TrigramSimilarity


class YoutubeDataService:

    @classmethod
    def search_youtube_data(self, search_description:str, search_title:str) -> dict:

        if not search_title and not search_description:
            return False, "Please enter valid param"

        elif search_title and not search_description:
            data_fetched = FetchedYoutubeData.objects.annotate(
                similarity=TrigramSimilarity("title", search_title)
            ).order_by("-similarity")
            return True, data_fetched

        elif not search_title and search_description:
            data_fetched = FetchedYoutubeData.objects.annotate(
                similarity=TrigramSimilarity("description", search_description)
            ).order_by("-similarity")
            return True, data_fetched

        else:
            return False, "Either title or description can be searched"
            