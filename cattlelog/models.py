from django.db import models

class cattle(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    sex=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    pub_date=models.DateTimeField('Date published : ')

class janu(models.Model):
    name=models.CharField(max_length=200,default='Janu')
    age=models.IntegerField(default=20)
    location=models.CharField(max_length=200,default='Kerala')
    sex=models.CharField(max_length=200,default='Female')
    arrival=models.CharField(max_length=200,default='January 26th')
    under=models.CharField(max_length=200,default='SangiYojana')


class ramu(models.Model):
    name=models.CharField(max_length=200,default='Ramu')
    age=models.IntegerField(default=28)
    location=models.CharField(max_length=200,default='Kochi')
    sex=models.CharField(max_length=200,default='Male')
    arrival=models.CharField(max_length=200,default='January 26th')
    under=models.CharField(max_length=200,default='SangiYojana')
