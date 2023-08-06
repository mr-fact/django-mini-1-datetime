from django.urls import path

from datetimenow.views import DateTimeNowView

urlpatterns = [
    path('<str:country>/', DateTimeNowView.as_view(), name='now-tmp-view-c'),
    path('', DateTimeNowView.as_view(), name='now-tmp-view'),
]
