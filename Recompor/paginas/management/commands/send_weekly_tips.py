from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from paginas.models import WeeklyTip, Notification

class Command(BaseCommand):
    help = 'Envia uma dica semanal para todos os usuários'

    def handle(self, *args, **kwargs):
        tip = WeeklyTip.objects.order_by('?').first()  # Pega uma dica aleatória
        if not tip:
            self.stdout.write(self.style.WARNING('Nenhuma dica cadastrada.'))
            return

        users = User.objects.all()
        for user in users:
            Notification.objects.create(
                user=user,
                message=f'<span class="dica-semanal">💡 Dica da semana: {tip.text}</span>'
            )
        self.stdout.write(self.style.SUCCESS('Dicas enviadas para todos os usuários!'))