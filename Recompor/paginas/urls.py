from django.urls import path
from .views import *

app_name= "paginas"

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('sobrenos/',SobreNosView.as_view(), name="sobrenos"),
    path('tutorialCaixa/', TutorialCaixaView.as_view(), name = "tutCaixa"),
    path('tutorialTerra/', TutorialTerraView.as_view(), name = "tutTerra"),
    path('materiaisCaixa/', MateriaisCaixaView.as_view(), name = "matCaixa"),
    path('materiaisTerra/', MateriaisTerraView.as_view(), name = "matTerra"),
    path('tutorialCaixa2', TutorialCaixa2View.as_view(), name = "tutCaixa2"),
    path('tutorialCaixa3', TutorialCaixa3View.as_view(), name = "tutCaixa3"),
    
]
