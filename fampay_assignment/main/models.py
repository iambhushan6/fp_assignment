from django.db import models

# Create your models here.

class FetchedYoutubeData(models.Model):

    unique_video_id = models.CharField(max_length=15,db_index=True)
    title = models.CharField(max_length=500, db_index=True)
    description = models.TextField()
    published_on = models.DateTimeField()
    thumbnail_url = models.URLField()

    class Meta:
        unique_together = ("unique_video_id","title","thumbnail_url")
        indexes = [
            models.Index(
                fields=[
                    "title",
                    "unique_video_id"
                ]
            ),
        ]