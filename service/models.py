from django.db import models
from django.contrib.auth.models import User
# from captcha.fields import CaptchaField

class Services(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_des = models.TextField()
    # captcha = CaptchaField()

class taskTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE,null=True,blank=True)
    Name = models.CharField(max_length=50)
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    # news_image = models.FileField(upload_to="news/", max_length=250, null=True,default=None)



