import pytz

from django.utils import timezone

class TimezoneMiddleware(object):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
            print "TimeZone activated: ", tzname
        else:
            timezone.deactivate()
            print "tzname = ", tzname
