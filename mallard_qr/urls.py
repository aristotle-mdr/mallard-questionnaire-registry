from django.conf.urls import include, patterns, url

#from mallard_qr import views#,forms
from django.views.generic import TemplateView
from aristotle_mdr.contrib.generic.views import GenericAlterManyToManyView

from aristotle_mdr.models import ValueDomain

from . import models
urlpatterns = patterns('mallard_qr.views',
    url(r'^question/(?P<iid>\d+)/responses/?$',
        GenericAlterManyToManyView.as_view(
            model_base = models.Question,
            model_to_add = ValueDomain,
            model_base_field = 'question',
        ), name='question_alter_responses'),

#These are required for about pages to work. Include them, or custom items will die!
#    url(r'^about/(?P<template>.+)/?$', views.DynamicTemplateView.as_view(), name="about"),
#    url(r'^about/?$', TemplateView.as_view(template_name='comet/static/about_comet_mdr.html'), name="about"),
)
