from django.db import models

class GetFormData(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField(max_length=500)


    def __str__(self):
        return "{}".format(name)