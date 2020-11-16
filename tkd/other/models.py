from django.db import models
from django.utils.html import mark_safe
from PIL import Image

class About(models.Model):
	about_us = models.TextField()

	def __str__(self):
		return "About Us"

class Contact(models.Model):
	platform = models.CharField(max_length=500)
	username = models.CharField(max_length=500)
	url = models.URLField(max_length=3000)

	def __str__(self):
		return self.platform +" - "+ self.username

class MainPhoto(models.Model):
	image = models.ImageField(upload_to='', help_text="Home page photo")

	def __str__(self):
		return "Main Photo"
	def save(self):
		# compress images
		super().save()
		if self.image:
			img = Image.open(self.image.path)
			output_size = (2000,1000)
			if (img.height > output_size[0] or img.width > output_size[1]):
				img.thumbnail(output_size)
				img.save(self.image.path)
	def image_tag(self):
		return mark_safe('<img src="/media/%s" height="300" />' % (self.image))
	image_tag.short_description = 'Image Preview'

class Time(models.Model):
	display_order = models.DecimalField(decimal_places=0, max_digits=2, help_text="Order to display (0 is displayed first)")
	day = models.CharField(max_length=50, help_text="Weekday")
	start = models.CharField(max_length=50, help_text="Start Time (Format: 00:00am)")
	end = models.CharField(max_length=50, help_text="Start Time (Format: 00:00pm)")

	def __str__(self):
		return str(self.display_order) + "." + self.day + " - " + self.start
	class Meta:
		ordering = ['display_order']

class PracticeTime(models.Model):
	location = models.CharField(max_length=500, help_text="Location of practices")
	times = models.ManyToManyField(Time, related_name='times')

	def __str__(self):
		return "Practice Times"

class Register(models.Model):
	url = models.URLField(max_length=3000, help_text="Link to register")

	def __str__(self):
		return "Register Link"