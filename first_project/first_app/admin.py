from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpages

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpages)
