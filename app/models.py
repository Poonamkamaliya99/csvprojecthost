from django.db import models

# Create your models here.

class Csv(models.Model):
    file_name=models.CharField( max_length=50)
    myfile=models.FileField( upload_to='csv', default="")
    uploaded=models.DateTimeField(auto_now_add=True)
    activated=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.file_name)
    
    
    
class Student(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    