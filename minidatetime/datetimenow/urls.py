from django.urls import path

from datetimenow.views import DateTimeNowView, JDateTimeNowView

urlpatterns = [
    path('jalali/<str:country>/', JDateTimeNowView.as_view(), name='j-now-tmp-view-c'),
    path('jalali/', JDateTimeNowView.as_view(), name='j-now-tmp-view'),
    path('<str:country>/', DateTimeNowView.as_view(), name='now-tmp-view-c'),
    path('', DateTimeNowView.as_view(), name='now-tmp-view'),
]
