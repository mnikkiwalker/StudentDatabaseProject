from django.db import models

# Create your models here.
class Student(models.Model):
    studentId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    grade = models.IntegerField(default=0)

    class Meta:
        db_table = 'students'