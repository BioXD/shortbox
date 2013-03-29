from django.db import models

class Publisher(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length = 120)
    parent = models.ForeignKey('self', blank = True, null = True)

class Series(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length = 200)
    volume = models.IntegerField(default = 1)
    publisher = models.ForeignKey(Publisher)
    
class Issue(models.Model):
    
    def __str__(self):
        return "#" + str(self.number)
    
    number = models.CharField(max_length = 8)
    series = models.ForeignKey(Series)
    pub_date = models.DateField('date published', blank = True)
    notes = models.TextField(blank = True)