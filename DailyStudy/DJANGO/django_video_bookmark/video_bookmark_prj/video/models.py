from django.db import models


class VideoCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    like_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    category = models.ForeignKey(VideoCategory)

    def __str__(self):
        return self.title

    def add_like_count(self):
        self.like_count += 1
