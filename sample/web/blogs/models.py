# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from tags.models import  TaggedItem

class Entry(models.Model):
    user  = models.ForeignKey(User,verbose_name=_(u'User') ) 
    title = models.CharField(_(u'Title'),max_length=200)
    text  = models.TextField(_(u'Text'),)
    tags = generic.GenericRelation( TaggedItem,
                limit_choices_to = {
                    'tag__content_type__name':u'entry',
                    'content_type__name':u'entry'}
                ) 

    def __unicode__(self):
        return self.title + " by " + self.user.__unicode__()

class Comment(models.Model):
    user  = models.ForeignKey(User,verbose_name=_(u'User') ,null=True,blank=True,default=None) 
    entry = models.ForeignKey(Entry,verbose_name=_(u'Entry') ) 
    text  = models.TextField(_(u'Text'))
    tags = generic.GenericRelation( TaggedItem,
                limit_choices_to = {
                    'tag__content_type__name':u'comment',
                    'content_type__name':u'comment'}
                ) 

    def __unicode__(self):
        return "Comment by " + self.user.__unicode__()
