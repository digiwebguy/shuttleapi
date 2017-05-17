"""shuttleapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from users import views as users_views
from trips import views as trips_views
from topups import views as topups_views
from drivers import views as drivers_views
from timestamp import views as timestamp_views
from shuttle_stations import views as shuttle_station_views
from shuttle_locations import views as shuttle_locations_views
from direction_options import views as direction_options_views
from alerts import views as alerts_views
from demo import views as demo_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/batch_trip_payment', users_views.PayForTrips.as_view()),
    url(r'^users/', users_views.UserList.as_view()),
    url(r'^topups/', topups_views.TopupsList.as_view()),
    url(r'^trips/', trips_views.TripsList.as_view()),
    url(r'^drivers/', drivers_views.DriversList.as_view()),
    url(r'^time/', timestamp_views.TimestampList.as_view()),
    # url(r'^smartgrid/users/TX149/lights-on', demo_views.TurnOnLights.as_view()),
    # url(r'^smartgrid/users/TX149/lights-on', demo_views.TurnOnLights.as_view()),
    # url(r'^smartgrid/(?P<pk>[0-9])/', demo_views.DemoList.as_view()),
    # url(r'^smartgrid/', demo_views.DemoList.as_view())
    url(r'^shuttle_stations/(?P<pk>[0-9])/direction_options/', direction_options_views.DirectionOptionsByShuttleStationId.as_view()),
    url(r'^shuttle_stations/', shuttle_station_views.ShuttleStationsList.as_view()),
    url(r'^shuttle_locations/(?P<pk>[0-9])/', shuttle_locations_views.ShuttleLocationsList.as_view()),
    url(r'^shuttle_locations/', shuttle_locations_views.ShuttleLocationsList.as_view()),
    url(r'^direction_options/', direction_options_views.DirectionOptionsList.as_view()),
    url(r'^alerts/', alerts_views.AlertsList.as_view()),
    url(r'^pending_alerts/', alerts_views.PendingAlertsList.as_view()),
    url(r'^pending_alerts_in_shuttle_stations/', shuttle_station_views.PendingAlertsInShuttleStationsList.as_view()),
    url(r'^accept_alerts/', alerts_views.AcceptAlerts.as_view()),
    # url(r'^topups/', topups_views.DoTopup.as_view())

    # url(r'^static/', )
]
