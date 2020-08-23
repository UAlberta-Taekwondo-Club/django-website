from django.contrib import admin
from .models import About, Contact, MainPhoto, PracticeTime, Register, Time

class MainPhotoAdmin(admin.ModelAdmin):
	readonly_fields = ['image_tag',]

admin.site.register(About)
admin.site.register(Contact)
admin.site.register(MainPhoto, MainPhotoAdmin)
admin.site.register(PracticeTime)
admin.site.register(Register)
admin.site.register(Time)