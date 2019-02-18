from django.conf.urls import url

from pretix.api.urls import orga_router

from . import views

urlpatterns = [
    url(r'^control/event/(?P<organizer>[^/]+)/prepared_templater/',
        views.OrganizerImportView.as_view(),
        name='import')
]