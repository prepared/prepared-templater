import csv
import json
import logging
from datetime import timedelta

from django.contrib import messages
from django.db.models import Count, Q
from django.db.models.functions import Concat
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.timezone import now
from django.utils.translation import ugettext as _
from django.views.generic import DetailView, ListView, View

from pretix.base.models import Organizer
from pretix.base.services.mail import SendMailException
from pretix.base.settings import SettingsSandbox
from pretix.base.templatetags.money import money_filter
from pretix.control.permissions import (
    EventPermissionRequiredMixin, OrganizerPermissionRequiredMixin,
)
from pretix.control.views.organizer import OrganizerDetailViewMixin

logger = logging.getLogger('pretix.plugins.prepared_templater')

from django.http import HttpResponse
from django.views import View

from prepared_templater.models import EventTemplate, SyncedEvent

class EventTemplates(ListView):
    model = EventTemplate
    context_object_name = 'event_templates'
    template_name = 'manage_templates_list.html'
    permission = 'has_organizer_permission'

    def get_queryset(self):
        if 'organizer' in self.kwargs:
            organizer_id = Organizer.objects.get(slug=self.kwargs['organizer'])
            qs = EventTemplate.objects.filter(
                organizer=organizer_id
            )

        return qs


class TemplatedEvents(View):
    def get(self, *args, **kwargs):
        if 'organizer' in self.kwargs:
            return HttpResponse('yay')
        else:
            return HttpResponse('na')