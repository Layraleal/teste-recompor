from django.views.generic import TemplateView
from django.http import HttpResponse
from composteira import *
from usuarios import *
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification

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


def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "notifications/notifications.html", {
        "notifications": notifications
    })

def mark_as_read(request, notif_id):
    notif = get_object_or_404(Notification, id=notif_id, user=request.user)
    notif.seen = True
    notif.save()
    return redirect("paginas:notifications")

def delete_notification(request, notif_id):
    notif = get_object_or_404(Notification, id=notif_id, user=request.user)
    notif.delete()
    return redirect("paginas:notifications")