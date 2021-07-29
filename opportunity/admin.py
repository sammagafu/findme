from django.contrib import admin
from .models import Opportunity,AppliedJob,SavedJob
# Register your models here.
admin.site.register(Opportunity)
admin.site.register(AppliedJob)
admin.site.register(SavedJob)