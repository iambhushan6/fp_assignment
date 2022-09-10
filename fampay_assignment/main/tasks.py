import requests
from fampay_assignment import settings
from datetime import datetime
from fampay_assignment.celery import app
from celery.schedules import crontab
from main.models import FetchedYoutubeData
from rest_framework.status import HTTP_200_OK

@app.task()
def fetch_youtube_data():
    """
    Task to be fired every 10 minutes to fetch youtube data, configured with crontab
    """

    published_after_timestamp = "2022-07-01T10:04:17.128280Z"
    search_query = "python"

    youtube_url = f"https://www.googleapis.com/youtube/v3/search?q={search_query}&order=date&publishedAfter={published_after_timestamp}&maxResults=50&part=snippet&key={settings.YOU_TUBE_API_KEY}"

    response_object = requests.get(youtube_url)       # Fetch data from youtubes url

    if response_object.status_code == HTTP_200_OK:
        
        instances_to_be_saved = []
        json_response = response_object.json()

        for response in json_response["items"]:

            unique_video_id = response["id"]["videoId"]
            title = response["snippet"]["title"]
            description = response["snippet"]["description"]
            thumbnail_url = response["snippet"]["thumbnails"]["default"]["url"]
            published_on = response["snippet"]["publishedAt"]

            if not FetchedYoutubeData.objects.filter(unique_video_id=unique_video_id).exists():
                published_datetime = datetime.strptime(
                    published_on, "%Y-%m-%dT%H:%M:%SZ"
                )
                instances_to_be_saved.append(
                    FetchedYoutubeData(
                        unique_video_id=unique_video_id,
                        title=title,
                        description=description,
                        thumbnail_url=thumbnail_url,
                        published_on=published_datetime,
                    )
                )

        if instances_to_be_saved:
            FetchedYoutubeData.objects.bulk_create(instances_to_be_saved)   # Bulk create instances here, we can make a logger to let us know about task completion

# I have made this task as for now scheduled for each 10 minutes

# Beast schedule of task

app.conf.beat_schedule = {
    "fetch_youtube_data_every_10_minute": {
        "task": "krypto_assignment.main.tasks.fetch_youtube_data",
        "schedule": crontab(minute='*/10'),
        "args": (),
    }
}