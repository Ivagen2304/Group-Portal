from django.core.management.base import BaseCommand
from django.utils import timezone
from moderation.models import Poll, Notification
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Send scheduled poll notifications'

    def handle(self, *args, **options):
        now = timezone.now()
        polls = Poll.objects.filter(sent=False, send_at__lte=now)
        User = get_user_model()
        users_qs = User.objects.filter(is_active=True)
        total = 0
        for p in polls:
            for u in users_qs:
                Notification.objects.create(user=u, poll=p, message=p.question)
                total += 1
            p.sent = True
            p.save()
        self.stdout.write(self.style.SUCCESS(f'Sent {total} notifications for {polls.count()} polls at {now}'))
