# Create your models here.

from django.db import models
from django.utils import timezone


class BusinessToNext(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.text)


class Concept(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)


class Plan(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)


class Design(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)


class Build(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)


class QualityAssurance(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)


class Delivery(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)


class About(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)


class Careers(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)


class Services(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Servicesdetail(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)


class Contact(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)
    
class NeedHelp(models.Model):
    phoneNumber = models.CharField(max_length=15, help_text='+92-0900-10072')    
    address = models.CharField(max_length=256, help_text='address', blank=True, null=True) 
    city = models.CharField(max_length=256, help_text='city' , blank=True, null=True)
    country = models.CharField(max_length=256, help_text='country' , blank=True, null=True)
    open_time = models.CharField(max_length=256, help_text='time' , blank=True, null=True)    
    closed = models.CharField(max_length=256, help_text='time', blank=True, null=True)    
    
    def __str__(self):
        return str(self.phoneNumber)