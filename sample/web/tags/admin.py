# -*- coding: utf-8 -*- 
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.conf import settings
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _ 

from models import *


### Tag 
class TagAdmin(admin.ModelAdmin):
    list_display=tuple([f.name for f in Tag._meta.fields ])
admin.site.register(Tag,TagAdmin)
