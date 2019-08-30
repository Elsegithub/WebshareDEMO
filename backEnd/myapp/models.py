from django.db import models

# Create your models here.
class test(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女')
    )

    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender,default='男')
    lrrq = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.username
    class Meta:
        ordering = ['lrrq']
        verbose_name = '用户'
        verbose_name_plural = '用户'

class textvue(models.Model):
    title = models.CharField(max_length=128)
    img = models.CharField(max_length=256)
    lrrq = models.DateTimeField(auto_now_add=True)
    txt = models.TextField()
    def _str_(self):
        return self.title