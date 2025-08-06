from django.views.generic import TemplateView
from django.http import HttpResponse
from composteira import *
from usuarios import *
from django.shortcuts import render, redirect

class IndexView(TemplateView):
    template_name = "home.html"
    
class SobreNosView(TemplateView):
    template_name = "sobrenos.html"

class MateriaisCaixaView(TemplateView):
    template_name = "materiaisCaixa.html"

class MateriaisTerraView(TemplateView):
    template_name = "materiaisTerra.html"

class TutorialCaixaView(TemplateView):
    template_name= "tutorialCaixa.html"

class TutorialTerraView(TemplateView):
    template_name = "tutorialTerra.html"

class TutorialCaixa2View(TemplateView):
    template_name = "tutorialCaixa2.html"

class TutorialCaixa3View(TemplateView):
    template_name = "tutorialCaixa3.html"        

