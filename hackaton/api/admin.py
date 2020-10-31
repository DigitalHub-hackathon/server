from django.contrib import admin
import api.models as models

admin.site.register(models.Organization)
admin.site.register(models.Group)