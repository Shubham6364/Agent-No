
from operator import mod
from pyexpat import model
from random import choices
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

#images
from io import BytesIO
from PIL import Image
from django.core.files import File



# Create your models here.

class Test(models.Model):
	firstname = models.TextField(max_length=40)
	lastname = models.TextField(max_length=40)


def compress(image):
	im = Image.open(image)
	im_io = BytesIO() 
	im.save(im_io, 'JPEG', quality=60) 
	new_image = File(im_io, name=image.name)
	return new_image


class Salepost(models.Model):
	STATUS = ('Publish','Publish'),('Draft','Draft')
	status = models.CharField(choices=STATUS, max_length=50,default='Draft')
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	property_type = models.TextField(max_length=10)
	area_type = models.TextField(max_length=10)
	floor = models.TextField(max_length=10)
	total_floor = models.TextField(max_length=10)
	property_age = models.TextField(max_length=10)
	property_status = models.TextField(max_length=10)
	land_mark = models.TextField(max_length=10)
	location = models.TextField(max_length=10)
	selling_price = models.TextField(max_length=10)
	date = models.DateField(max_length=5,blank=True, null=True)
	furnishing =  models.TextField(max_length=10)
	description = models.TextField(max_length=20)
	video = models.FileField(upload_to='')
	areasqt = models.TextField(max_length=4)
	multiple = models.TextField(max_length=4)	
	Buy = models.CharField(max_length=10)
	lift = models.CharField(max_length=10,blank=True,null=True)
	gym = models.CharField(max_length=10,blank=True,null=True)
	swimmingpool = models.CharField(max_length=10,blank=True,null=True)
	petsallowed = models.CharField(max_length=10,blank=True,null=True)
	wifiinternet = models.CharField(max_length=10,blank=True,null=True)
	childrenPlayground = models.CharField(max_length=10,blank=True,null=True)
	twowheeler = models.CharField(max_length=10,blank=True,null=True)
	fourwheeler = models.CharField(max_length=10,blank=True,null=True)
	towfourwheeler = models.CharField(max_length=10,blank=True,null=True)
	gateaccess = models.CharField(max_length=10,blank=True,null=True)
	balcony = models.CharField(max_length=10,blank=True,null=True)
	isDelete = models.BooleanField(default=False)
	new_slug=AutoSlugField(populate_from='property_type',unique=True,default=None)
	image1 = models.ImageField(upload_to='views', blank=True, null=True ,default='profile_img/925667.jpg')
	image2 = models.ImageField(upload_to='views', blank=True, null=True , default='profile_img/925667.jpg')
	imag3 = models.ImageField(upload_to='views', blank=True, null=True ,default='profile_img/925667.jpg')
	
	def image1_url(self):   
		if self.image1 and hasattr(self.image1, 'url'):       
					return self.image1.url
	def image2_url(self):   
		if self.image2 and hasattr(self.image2, 'url'):       
					return self.image2.url

	def imag3_url(self):   
		if self.image3 and hasattr(self.imag3, 'url'):       
					return self.imag3.url

	
    
	

	def save(self, *args, **kwargs):
		new_image = compress(self.image1)
		self.image1 = new_image
		super().save(*args, **kwargs)

			
	

	

		





class Rentpost(models.Model):
	STATUS = ('Publish','Publish'),('Draft','Draft')
	status = models.CharField(choices=STATUS, max_length=50,default='Draft')
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	property_type = models.TextField(max_length=1)
	area_type = models.TextField(max_length=1)
	floor = models.TextField(max_length=1)
	totalfloor = models.TextField(max_length=1)
	propertyage = models.TextField(max_length=1)
	propertystatus = models.TextField(max_length=1)
	landmark = models.TextField(max_length=1)
	location = models.TextField(max_length=1)
	askingrent = models.TextField(max_length=1)
	askingdeposite = models.TextField(max_length=1)
	date = models.DateField(max_length=5)
	furnishing =  models.TextField(max_length=1)
	description = models.TextField(max_length=1)
	image = models.FileField(upload_to='media')
	video = models.FileField(upload_to='media')
	areasqt = models.TextField(max_length=1)		
	multiple = models.TextField(max_length=1)
	rent = models.CharField(max_length=10)
	isDelete = models.BooleanField(default=False)
	

class Stafflogin(models.Model):
	fname = models.CharField(max_length=10)
	lname = models.CharField(max_length=10)
	username = models.CharField(max_length=10)
	password = models.CharField(max_length=10)
	rpassword = models.CharField(max_length=10)


class Employee(models.Model):
	name = models.CharField(max_length=24)
	email = models.EmailField(max_length=24)
	address = models.TextField()
	phone = models.IntegerField()



