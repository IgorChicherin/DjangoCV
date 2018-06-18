from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from easy_thumbnails.fields import ThumbnailerImageField



# Create your models here.

class Portfolio(models.Model):
    img = ThumbnailerImageField(upload_to='portfolio', null=True, blank=True)
    work_name = models.CharField(max_length=100)
    link = models.URLField(max_length=250, null=True)
    text = models.TextField()
    tag = models.CharField(max_length=50)

    def __str__(self):
        return str(self.work_name)

# @receiver(pre_save, Portfolio)
# def fix_path()



class Education(models.Model):
    img = ThumbnailerImageField(upload_to='education', null=True, blank=True)
    course = models.CharField(max_length=100)
    text = models.TextField()
    tag = models.TextField(max_length=50)

    def __str__(self):
        return str(self.course)


class Company(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=150)
    phonenum = models.IntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.name


class Work(models.Model):
    position = models.CharField(max_length=100)
    img = ThumbnailerImageField(upload_to='work', null=True, blank=True)
    company = models.ForeignKey(Company, null=True)
    link = models.URLField(max_length=250)
    text = models.TextField()
    date = models.CharField(max_length=200)

    def __str__(self):
        return '{} - {}'.format(self.company, self.position)
