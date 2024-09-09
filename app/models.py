from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=40)
    sage=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.sname