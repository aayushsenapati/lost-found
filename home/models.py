from django.db import models

class Reported(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to = 'lost_items/')
    srn = models.CharField(null=True,max_length=13)




