from django.db import models

class register(models.Model):
    Username=models.CharField(max_length=30)
    Email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=30)
    Phone=models.CharField(max_length=10)
    desig=models.CharField(max_length=13,default="user")

    def __str__(self):
        return self.Email


class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name
