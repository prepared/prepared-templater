from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = 'prepared_templater'
    verbose_name = 'Prepared Templater'

    class PretixPluginMeta:
        name = ugettext_lazy('Prepared Templater')
        author = 'Lukas Bockstaller'
        description = ugettext_lazy('Allows to use a pretix event as a template for further events')
        visible = True
        version = '1.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'prepared_templater.PluginApp'
