from django.db import models

from django.db import models

class Sign_Up(models.Model):
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   dob = models.IntegerField()
   email = models.CharField(max_length=50)
   phone_num = models.IntegerField()
   sign_date = models.DateTimeField()

class user_log_in(models.Model):
   sign_up = models.ForeignKey(Sign_Up, on_delete=models.CASCADE)
   


    
