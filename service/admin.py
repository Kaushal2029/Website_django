from django.contrib import admin
from service.models import *


class serviceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des','user')

class tableAdmin(admin.ModelAdmin):
    list_display=('Name','Title','Description', 'service')


admin.site.register(Services,serviceAdmin)
admin.site.register(taskTable,tableAdmin)
# Register your models here.
