from django.db import models

# Create your models here.

class User(models.Model):

    username = models.CharField(max_length = 30, primary_key = True)

    first_name = models.CharField(max_length = 30)

    last_name = models.CharField(max_length = 30)

    # the email address should not be used by any other user in the system
    email = models.EmailField(unique = True)

    # whether the user is an instructor (or student)
    is_instructor = models.BooleanField()

    
class Course(models.Model):

    course_id = models.IntegerField(primary_key = True)

    course_name = models.CharField(max_length = 128)  

    instructor = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    
    start_date = models.DateField()
    
    end_date = models.DateField()

    # meeting time/frequency of the course
    meet_freq = models.CharField(max_length = 256)    
    
    
class Enrollment(models.Model):

    enroll_id = models.AutoField(primary_key = True)
    
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    
    student = models.ForeignKey(User, on_delete = models.CASCADE)

    
class Code(models.Model):

    # a random string used to generate a QR code
    class_code = models.CharField(primary_key = True, max_length = 256)
    
    create_time = models.DateTimeField()
    
    course = models.ForeignKey(Course, on_delete = models.SET_NULL, null = True)
    

class Attendance(models.Model):

    attendance_id = models.AutoField(primary_key = True)

    image = models.ImageField()
    
    upload_time = models.DateTimeField()
    
    student = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    
    code = models.ForeignKey(Code, on_delete = models.SET_NULL, null = True)



