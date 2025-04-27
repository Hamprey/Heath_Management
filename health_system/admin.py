from django.contrib import admin
from .models import Client, HealthProgram, Enrollment

admin.site.register(Client)
admin.site.register(HealthProgram)
admin.site.register(Enrollment)

