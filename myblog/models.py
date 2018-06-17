from django.db import models


# Create your models here.

class Portfolio(models.Model):
    img = models.CharField(max_length=150)
    work_name = models.CharField(max_length=100)
    link = models.URLField(max_length=250, null=True)
    text = models.TextField()
    tag = models.CharField(max_length=50)

    def __str__(self):
        return str(self.work_name)


class Education(models.Model):
    img = models.CharField(max_length=150)
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
    img = models.CharField(max_length=150)
    company = models.ForeignKey(Company, null=True)
    link = models.URLField(max_length=250)
    text = models.TextField()
    date = models.CharField(max_length=200)

    def __str__(self):
        return '{} - {}'.format(self.company, self.position)
