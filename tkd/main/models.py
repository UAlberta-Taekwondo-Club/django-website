from django.db import models
from django.utils import timezone
from PIL import Image
from django.utils.html import mark_safe
from datetime import datetime

class Announcement(models.Model):
	pinned = models.BooleanField(default=False, help_text="Pin Announcement")
	title = models.CharField(max_length=500)
	title_link = models.URLField(max_length=3000, help_text="(optional) Redirect URL for title", null=True, blank=True)
	description = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='announcement', help_text="(optional)" ,null=True, blank=True)

	def __str__(self):
		# django admin will show announcement's title
		if self.pinned == True:
			return "[PINNED] "+self.title
		return self.title
	def save(self):
		# compress images
		super().save()
		if self.image:
			img = Image.open(self.image.path)
			output_size = (300,300)
			if (img.height > output_size[0] or img.width > output_size[1]):
				img.thumbnail(output_size)
				img.save(self.image.path)
	def image_tag(self):
		return mark_safe('<img src="/media/%s" height="150" />' % (self.image))
	image_tag.short_description = 'Image Preview'
	class Meta:
		ordering = ['-date_posted']

class Event(models.Model):
	title = models.CharField(max_length=500)
	start = models.DateTimeField()
	end = models.DateTimeField()
	location = models.CharField(max_length=500)
	cost = models.DecimalField(decimal_places=2, max_digits=500, default=0)
	details = models.TextField()
	button_url = models.URLField(max_length=3000, help_text="(optional) URL to direct to", null=True, blank=True)
	button_label = models.CharField(max_length=100, help_text="(optional) Text on link button", null=True, blank=True)

	def __str__(self):
		return self.title
	class Meta:
		ordering = ['start']

class Exec(models.Model):
	name = models.CharField(max_length=500)
	position = models.CharField(max_length=500)
	detail = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='profile')

	def __str__(self):
		return self.name
	def save(self):
		# compress images
		super().save()
		img = Image.open(self.image.path)
		output_size = (200,200)
		if (img.height > output_size[0] or img.width > output_size[1]):
			img.thumbnail(output_size)
			img.save(self.image.path)
	def image_tag(self):
		return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))
	image_tag.short_description = 'Image Preview'
	class Meta:
		ordering = ['name']

class FAQ(models.Model):
	question = models.TextField()
	answer = models.TextField()
	def __str__(self):
		return self.question

class Form(models.Model):
	title = models.CharField(max_length=500)
	date_posted = models.DateTimeField(default=timezone.now)
	url = models.URLField(max_length=3000)
	def __str__(self):
		return self.title
	class Meta:
		ordering = ['-date_posted']

class Mentor(models.Model):
	name = models.CharField(max_length=500)
	position = models.CharField(max_length=500, null=True, blank=True)
	detail = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='profile')

	def __str__(self):
		return self.name
	def save(self):
		# compress images
		super().save()
		img = Image.open(self.image.path)
		output_size = (200,200)
		if (img.height > output_size[0] or img.width > output_size[1]):
			img.thumbnail(output_size)
			img.save(self.image.path)
	def image_tag(self):
		return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))
	image_tag.short_description = 'Image Preview'
	class Meta:
		ordering = ['name']

class Photo(models.Model):
	name = models.CharField(max_length=500, default="Photo")
	date_taken = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='gallery')

	def __str__(self):
		return self.name
	def save(self):
		super().save()
		# open image
		img = Image.open(self.image.path)
		try:
			# set photo name from image
			self.date_taken = datetime.strptime(img._getexif()[306], "%Y:%m:%d %H:%M:%S")
			# set image name from image
			self.name = self.image.path.split('/')[-1]
		except:
			pass
		# save model
		super().save()
		# compress images
		output_size = (800,800)
		if (img.height > output_size[0] or img.width > output_size[1]):
			img.thumbnail(output_size)
			img.save(self.image.path)
	def image_tag(self):
		return mark_safe('<img src="/media/%s" height="400" />' % (self.image))
	image_tag.short_description = 'Image Preview'
	class Meta:
		ordering = ['name']