from django.conf.urls import url

from pretix.api.urls import orga_router

from . import views

urlpatterns = [
    url(r'^control/organizer/(?P<organizer>[^/]+)/prepared_templater/manage_event_templates',
        views.EventTemplates.as_view(),
        name='manage_event_templates'),
    url(r'^control/organizer/(?P<organizer>[^/]+)/prepared_templater/manage_events',
        views.TemplatedEvents.as_view(),
        name='manage_events')
]