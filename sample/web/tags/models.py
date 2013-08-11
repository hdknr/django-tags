# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User

class TagManager(models.Manager):
    def get_for_model(self,name,model):
        return self.get_or_create(
                name = name, 
                    content_type = ContentType.objects.get_for_model(model)
               )

class Tag(models.Model):
    content_type = models.ForeignKey(ContentType, verbose_name=_('content type'))
    name = models.CharField(_(u'Name'),max_length=100,db_index=True,)

    def __init__(self,*args,**kwargs):
        super(Tag,self).__init__(*args,**kwargs)

    def __unicode__(self):
        return self.name

    objects = TagManager()

    class Meta:
        unique_together=('content_type','name',)

class TaggedItemManager(models.Manager):
    pass

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag)
    content_type = models.ForeignKey(ContentType, verbose_name=_('content type'))
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User)

    objects = TaggedItemManager()

    def save(self,*args,**kwargs):
        if self.tag and self.content_type and self.tag.content_type != self.content_type:
            return 
        super(TaggedItem,self).save(*args,**kwargs) 

    def __unicode__(self):
        return  self.tag.__unicode__() +" for " + self.content_type.__unicode__() 
    class Meta:
        unique_together=('tag','content_type','object_id','user',)
