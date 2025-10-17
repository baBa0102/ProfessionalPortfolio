from django.contrib import admin
from .models import Experience, Education, Resume, AdditionalSection

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Resume)
admin.site.register(AdditionalSection)