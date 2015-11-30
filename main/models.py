from django.db import models


class Host(models.Model):
    hostname = models.CharField(max_length=255)

    def __unicode__(self):
        return self.hostname

    class Meta:
        ordering = ('hostname',)


class Ping(models.Model):
    host = models.ForeignKey('main.Host')
    success = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
