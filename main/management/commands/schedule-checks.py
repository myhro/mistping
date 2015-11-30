from datetime import datetime
from django.core.management.base import BaseCommand
import django_rq
from main.tasks import check_all_hosts


class Command(BaseCommand):
    help = u'Schedule "check_all_hosts" task'

    def handle(self, *args, **options):
        scheduler = django_rq.get_scheduler('default')

        self.stdout.write('Clearing previous scheduled jobs...')
        for job in scheduler.get_jobs():
            job.cancel()

        self.stdout.write(u'Scheduling "check_all_hosts" task...')
        scheduler.schedule(
            scheduled_time=datetime.utcnow(),
            func=check_all_hosts,
            interval=60,
            repeat=None,
        )

        self.stdout.write('Done.')
