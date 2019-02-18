from django.dispatch import receiver
from django.template.loader import get_template
from django.urls import resolve, reverse
from django.utils.translation import ugettext_lazy as _

from pretix.base.signals import register_payment_providers
from pretix.control.signals import nav_organizer


@receiver(nav_organizer, dispatch_uid="prepared_templater_organav")
def control_nav_orga_import(sender, request=None, **kwargs):
    url = resolve(request.path_info)
    return [
        {
            'label': _('Event Templates'),
            'url': reverse('plugins:prepared_templater:import', kwargs={
                'organizer': request.organizer.slug,
            }),
            'active': (url.namespace == 'plugins:prepared_templater:import' and url.url_name == 'import'),
            'icon': 'clone',
            'children': [
                {
                    'label': _('Manage Event Templates'),
                    'url': reverse('plugins:prepared_templater:import', kwargs={
                        'organizer': request.organizer.slug,
                    }),
                    'active': (url.namespace == 'plugins:prepared_templater:import' and url.url_name == 'import'),
                    'icon': 'clone',
                },
                {
                    'label': _('Create new Events'),
                    'url': reverse('plugins:prepared_templater:import', kwargs={
                        'organizer': request.organizer.slug,
                    }),
                    'active': (url.namespace == 'plugins:prepared_templater:import' and url.url_name == 'import'),
                    'icon': 'clone',
                }

            ]
        }
    ]