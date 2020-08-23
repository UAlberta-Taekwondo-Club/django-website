from django.contrib import admin
from .models import Announcement, Event, Exec, FAQ, Form, Mentor, Photo

# show images in django admin
class AnnouncementAdmin(admin.ModelAdmin):
	readonly_fields = ['image_tag',]
class ExecAdmin(admin.ModelAdmin):
	readonly_fields = ['image_tag',]
class MentorAdmin(admin.ModelAdmin):
	readonly_fields = ['image_tag',]
class PhotoAdmin(admin.ModelAdmin):
	readonly_fields = ['image_tag',]

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Event)
admin.site.register(Exec, ExecAdmin)
admin.site.register(FAQ)
admin.site.register(Form)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Photo, PhotoAdmin)