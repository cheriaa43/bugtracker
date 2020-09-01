from django.contrib import admin
from bugtracker_app.models import CustomUser, Ticket

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Ticket)