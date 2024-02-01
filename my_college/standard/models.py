from django.db import models

# Create your models here.
class Section(models.Model):
    sectionname=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.sectionname
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    roll_Number = models.IntegerField(null=True)
    DOB = models.DateField(null=True)
    section = models.ForeignKey(
        "Section", on_delete=models.CASCADE)

  
 