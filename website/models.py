from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MaxValueValidator, MinValueValidator


# class UserAccount(AbstractUser):
#     id = models.AutoField(primary_key=True)
#     #built in username and password
#     grade_level = models.IntegerField()
                    
#     def __str__(self):
#         return self.username

class Department(models.Model):
    code = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=40)

    def __str__(self):
      return self.name

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=69)
    course_number = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField()
    flagged = models.BooleanField(default=False, blank=True)

    def get_absolute_url(self):
      return f'elective/{self.department.code}/{self.course_number}'

    def __str__(self):
      return str(self.department.code) + " "+str(self.course_number) + " "+self.name


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    def __str__(self):
      return str(self.first_name) + " " + str(self.last_name)
    class Meta:
        abstract = True

class Professor(Teacher):
    prefix = models.BooleanField()
    office = models.CharField(max_length=15)

class GraduateStudent(Teacher):
    grade_level = models.IntegerField(default=0)

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    rating_positive = models.IntegerField(default=0)
    rating_negative = models.IntegerField(default=0)
    last_modified = models.DateTimeField(auto_now=True)
    year_taken = models.PositiveSmallIntegerField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    flagged = models.BooleanField(default=False)

    def __str__(self):
      return str(self.author.username) + ", for " +str(self.course.name) + ", at " + str(self.last_modified)

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    query = models.TextField(max_length=100)

    def __str__(self):
      return str(self.email + " SENT: " + self.query)