from django.shortcuts import render
from .models import Announcement, Event, Exec, FAQ, Form, Mentor, Photo
from other.models import About, Contact, MainPhoto, PracticeTime, Register
from django.utils import timezone

def home(request):
	context = {
		'contacts':Contact.objects.all(),
		'main_photo':MainPhoto.objects.first(),
		'register':Register.objects.first(),
		'announcements':Announcement.objects.all(),
		'events':Event.objects.all().filter(start__date__gte=timezone.now().date()),
		'forms':Form.objects.all(),
		'practice_times':PracticeTime.objects.first(),
	}
	return render(request, 'main/home.html', context)

def about(request):
	context = {
		'about':About.objects.first(),
		'contacts':Contact.objects.all(),
		'execs':Exec.objects.all(),
		'mentors':Mentor.objects.all(),
		'FAQs':FAQ.objects.all(),
		'main_photo':MainPhoto.objects.first(),
		'register':Register.objects.first()
	}
	return render(request, 'main/about.html', context)

def announcements(request):
	context = {
		'pinned':Announcement.objects.all().filter(pinned=True),
		'announcements':Announcement.objects.all().filter(pinned=False)
	}
	return render(request, 'main/announcements.html', context)

def events_calendar(request):
	return render(request, 'main/event_calendar.html')

def events_list(request):
	context = {
		'events':Event.objects.all().filter(start__date__gte=timezone.now().date())
	}
	return render(request, 'main/events_list.html', context)

def events_past(request):
	context = {
		'events':Event.objects.filter(start__date__lt=timezone.now().date()).order_by('-start'),
	}
	return render(request, 'main/events_past.html', context)

def forms(request, id):
	print(id)
	if id == 0:
		# no forms
		return render(request, 'main/forms.html')
	context = {
		'selected_form':Form.objects.get(id=id),
		'forms':Form.objects.all()
	}
	return render(request, 'main/forms.html', context)

def gallery(request):
	photos = Photo.objects.all().order_by('-date_taken')
	context = {
		'youtube_url':Contact.objects.filter(platform__iexact='youtube').first(),
		'photos':photos,
		'first':photos.first()
	}
	return render(request, 'main/gallery.html', context)

def gallery_photo(request, id):
	photo = Photo.objects.get(id=id)
	context = {
		'photo':photo,
		'previous':Photo.objects.filter(date_taken__gt=photo.date_taken).order_by('date_taken').first(),
		'next':Photo.objects.filter(date_taken__lt=photo.date_taken).order_by('-date_taken').first()
	}
	return render(request, 'main/photo.html', context)