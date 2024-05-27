from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=250)
    file = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name

    class Meta:
        app_label = "blog"
