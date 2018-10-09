from django.db import models


class CSVData(models.Model):
    key = models.CharField(max_length=100)
    value = models.IntegerField()
