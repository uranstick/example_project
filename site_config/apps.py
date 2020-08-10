from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SiteConfig(AppConfig):
    name = 'example.site_config'
    verbose_name = _('Site config')
