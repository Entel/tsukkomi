from tsukkomi.models import *
from django.contrib import admin

# Register your models here.
class ContentAdmin(admin.ModelAdmin):
	fieldsets = [
		#('id', {'fields': ['id']}),
		('text', {'fields': ['text']}),
		('ip', {'fields': ['ip']}),
		('publish time', {'fields': ['time']}),
	]
admin.site.register(Content, ContentAdmin)
admin.site.register(Rate)
admin.site.register(Comment)
	
