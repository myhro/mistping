import logging
import subprocess
import django_rq
from .models import Host
from .models import Ping


def check_all_hosts():
    hosts = Host.objects.all()
    for h in hosts:
        check_host.delay(h.pk)

@django_rq.job
def check_host(host_id):
    logging.basicConfig()
    host = Host.objects.get(pk=host_id)
    logging.info('Checking ' + host.hostname)
    proc = subprocess.Popen(['ping', '-c 4', host.hostname], stdout=subprocess.PIPE)
    return_code = proc.wait()
    success = not bool(return_code)
    Ping(host=host, success=success).save()
    logging.info('Check for {host} saved.'.format(host=host.hostname))
