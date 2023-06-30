from django.contrib import admin
from .models import Project, Review, Tag

class ProjectAdmin(admin.ModelAdmin):
    list_display= ['title', 'owner']
# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Review)
admin.site.register(Tag)



