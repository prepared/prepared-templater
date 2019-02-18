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

from pretix.base.models import Order, OrderPayment, Quota
from pretix.base.services.mail import SendMailException
from pretix.base.settings import SettingsSandbox
from pretix.base.templatetags.money import money_filter
from pretix.control.permissions import (
    EventPermissionRequiredMixin, OrganizerPermissionRequiredMixin,
)
from pretix.control.views.organizer import OrganizerDetailViewMixin
from pretix.plugins.banktransfer import csvimport, mt940import
from pretix.plugins.banktransfer.models import BankImportJob, BankTransaction
from pretix.plugins.banktransfer.tasks import process_banktransfers

logger = logging.getLogger('pretix.plugins.prepared_templater')

from django.http import HttpResponse
from django.views import View

from prepared_templater.models import EventTemplate, SyncedEvent

class HelloWorld(View):
    def get(self, *args, **kwargs):
        # <view logic>
        return HttpResponse('HelloWorld')

class EventTemplates(View):
    def get(self, *args, **kwargs):
        if 'organizer' in self.kwargs:
            return HttpResponse('yay')
        else:
            return HttpResponse('na')