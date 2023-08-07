from datetime import datetime
import pytz

from django.shortcuts import render, Http404
from django.views.generic import TemplateView

import datetimenow


class DateTimeNowView(TemplateView):
    template_name = 'now.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        country_code = self.kwargs.get('country', None)
        if country_code:
            try:
                time_zone = pytz.country_timezones[country_code.upper()][0]
                now_datetime = datetime.now().astimezone(pytz.timezone(time_zone))
            except Exception as e:
                raise Http404(e)
        else:
            now_datetime = datetime.now()
        context['country'] = country_code
        context['now'] = now_datetime.strftime('%Y-%m-%d %H:%M:%S')
        datetime_list = [
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
        context['datetime_list'] = [[d[0], d[1], now_datetime.strftime(d[0])] for d in datetime_list]
        return context
