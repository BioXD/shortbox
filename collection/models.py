from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length = 100)
    parent = models.ForeignKey('self')

class Series(models.Model):
    name = models.CharField(max_length = 200)
    volume = models.IntegerField(default = 1)
    publisher = models.ForeignKey(Publisher)
    
class Issue(models.Model):
    number = models.CharField(max_length = 10)
    pub_date = models.DateField('date published')
    notes = models.TextField()