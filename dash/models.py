from django.db import models


class File(models.Model):
    file_name = models.CharField(max_length=120, null=True, blank=True)
    file = models.FileField(upload_to="raw/", null=True, blank=True)
    slug = models.SlugField(max_length=20, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file_name)

class ProcessLog(models.Model):
    source_file = models.CharField(max_length=120, null=True, blank=True)
    file_created = models.IntegerField(null=True, blank=True)
    verdict = models.BooleanField(default=True)
    task = models.IntegerField(null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.source_file)