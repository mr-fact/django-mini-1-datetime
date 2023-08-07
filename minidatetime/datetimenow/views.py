from datetime import datetime

import jdatetime
import pytz

from django.shortcuts import render, Http404
from django.views.generic import TemplateView

import datetimenow


class BaseDateTimeNowView(TemplateView):
    template_name = 'now.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.datetime_list = [
            ('%D', '(DATE)'),
            ('%s', '(date to seconds)'),
            ('%Y', '4-digit year (e.g., 2023)'),
            ('%y', '2-digit year (e.g., 23)'),
            ('%h', 'Abbreviated month name (e.g., Jan)'),
            ('%b', 'Abbreviated month name (e.g., Jan)'),
            ('%m', '2-digit month (01 to 12)'),
            ('%B', 'Full month name (e.g., January)'),
            ('%d', '(day)'),
            ('%I', '12-hour format (01 to 12)'),
            ('%H', '24-hour format (00 to 23)'),
            ('%M', '2-digit minute (00 to 59)'),
            ('%S', '2-digit second (00 to 59)'),
            ('%P', 'PM / AM'),
            ('%p', 'pm / am'),
            ('%A', 'Full weekday name (e.g., Sunday)'),
            ('%a', 'Abbreviated weekday name (e.g., Sun)'),
            ('%Z', 'Timezone name'),
            ('%z', 'UTC offset (e.g., +0000)'),
        ]

    def get_now(self, time_zone=None):
        if time_zone:
            return datetime.now().astimezone(pytz.timezone(time_zone))
        return datetime.now()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        country_code = self.kwargs.get('country', None)
        if country_code:
            try:
                country_code = country_code.upper()
                time_zone = pytz.country_timezones[country_code][0]
                now_datetime = self.get_now(time_zone)
            except Exception as e:
                raise Http404(e)
        else:
            now_datetime = self.get_now()
        context['country'] = country_code
        context['now'] = now_datetime.strftime('%Y-%m-%d %H:%M:%S')
        result = []
        for d in self.datetime_list:
            if '%' in now_datetime.strftime(d[0]):
                result.append([d[1], d[0], ''])
            else:
                result.append([d[1], d[0], now_datetime.strftime(d[0])])
        context['datetime_list'] = result
        return context


class DateTimeNowView(BaseDateTimeNowView):
    pass


class JDateTimeNowView(BaseDateTimeNowView):
    def get_now(self, time_zone=None):
        if time_zone:
            return jdatetime.datetime.now().astimezone(pytz.timezone(time_zone))
        return jdatetime.datetime.now()
