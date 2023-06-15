from django.db import models

# Create your models here.
class Student(models.Model):
    Student_name=models.CharField(max_length=50,)
    id=models.IntegerField(max_length=5,primary_key=True)
    subjects=models.CharField(max_length=10)

class College(models.Model):
    Student_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    College_name=models.CharField(max_length=50)
    id=models.IntegerField(max_length=5,primary_key=True)
    course=models.CharField(max_length=10)
    

class InterBoard(models.Model):
    College_name=models.ForeignKey(College,on_delete=models.CASCADE)
    percentage=models.IntegerField(max_length=3.2)
    state=models.CharField(max_length=20)
