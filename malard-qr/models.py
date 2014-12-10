from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from model_utils import Choices

from tinymce.models import HTMLField
import aristotle_mdr as aristotle

class AdministrationMode(aristotle.models.unmanagedObject):
    pass

class Question(aristotle.models.concept):
    template = "mallard-qr/question.html"
    collected_data_element = models.ForeignKey(aristotle.models.DataElement,blank=True,null=True,related="questions")
    response_value_domain = models.ManyToManyField(aristotle.models.ValueDomain,verbose_name = "Value Domain",blank=True,null=True)
    question_text = HTMLField(blank=True)
    instruction_text = HTMLField(blank=True)
    administration_modes = models.ManyToManyField(AdministrationMode,blank=True,null=True)
    
class QuestionModule(aristotle.models.concept):
    template = "mallard-qr/questionmodule.html"
    questions = models.ManyToManyField(Question,blank=True,null=True)
    submodules = models.ManyToManyField('QuestionModule',blank=True,null=True)
    instruction_text = HTMLField(blank=True,null=True)
    sqbl_definition = TextField(blank=True,null=True)
    administration_modes = models.ManyToManyField(AdministrationMode,blank=True,null=True)
    
class Questionnaire(aristotle.models.concept):
    template = "mallard-qr/questionnaire.html"
    submodules = models.ManyToManyField(QuestionModule,blank=True,null=True)
    instructionText = HTMLField(blank=True)
    administration_modes = models.ManyToManyField(AdministrationMode,blank=True,null=True)
