from django.db import models

# Create your models here.

#模型类
class Student(models.Model):
    sname = models.CharField(max_length=30,unique=True)
    spwd = models.CharField(max_length=30)

    def __str__(self):
        return u'Student:%s'%self.sname