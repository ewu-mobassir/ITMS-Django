from django.db import models


class District(models.Model):
    district_name = models.CharField(max_length=100, verbose_name="District Name")

    def __str__(self):
        return self.district_name
# Create your models here.
