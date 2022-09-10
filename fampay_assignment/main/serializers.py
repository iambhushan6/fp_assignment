from rest_framework import serializers
from main.models import FetchedYoutubeData

class FetchedYoutubeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FetchedYoutubeData
        fields = "__all__"