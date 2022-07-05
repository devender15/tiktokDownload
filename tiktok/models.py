from django.db import models


class Videos(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    videoUrl = models.CharField(max_length=500)
    videoDownloadUrl = models.CharField(max_length=500, null=False)
    downloadDate = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return str(self.downloadDate) + " " + self.name
