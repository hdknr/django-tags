# -*- coding: utf-8 -*- 
from django import forms
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.conf import settings
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from models import *
from tags.models import Tag,TaggedItem

class CommentTaggedItemForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(CommentTaggedItemForm,self).__init__(*args,**kwargs)
        self.fields['tag'].queryset = Tag.objects.filter(content_type = ContentType.objects.get_for_model(Comment))

class EntryTaggedItemForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(EntryTaggedItemForm,self).__init__(*args,**kwargs)
        self.fields['tag'].queryset = Tag.objects.filter(content_type = ContentType.objects.get_for_model(Entry))

class CommentTaggedItemInline(generic.GenericTabularInline):
    model=TaggedItem
    form = CommentTaggedItemForm  

class EntryTaggedItemInline(generic.GenericTabularInline):
    model=TaggedItem
    form = EntryTaggedItemForm  

### Entry 
class EntryAdmin(admin.ModelAdmin):
    list_display=tuple([f.name for f in Entry._meta.fields ])
    inlines=[EntryTaggedItemInline,]
admin.site.register(Entry,EntryAdmin)

### Comment 
class CommentAdmin(admin.ModelAdmin):
    list_display=tuple([f.name for f in Comment._meta.fields ])
    inlines=[CommentTaggedItemInline,]
admin.site.register(Comment,CommentAdmin)

