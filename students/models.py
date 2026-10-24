from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}-{self.id}"

class Student(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')   
    dob = models.DateField()
    photo = models.ImageField(upload_to="student_profile",null =True , blank = True)
    
    def __str__(self):
        return f"Name : {self.name} -- Course : {self.course}"
    