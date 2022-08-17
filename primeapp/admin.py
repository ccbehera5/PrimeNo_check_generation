from django.contrib import admin
from primeapp.models import Savedata

# Register your models here.
class ModelSavedata(admin.ModelAdmin):
    list_display=['id','startno','stopno','outdata1','outdata2','time']
admin.site.register(Savedata,ModelSavedata)
