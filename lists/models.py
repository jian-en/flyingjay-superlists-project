from django.db import models


class List(models.Model):
    id = models.AutoField(primary_key=True)


class Item(models.Model):
    text = models.TextField()
    list = models.ForeignKey(List)
