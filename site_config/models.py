from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

from .abstract_models import SingletonModel


class SiteConfig(SingletonModel):

    user_message = RichTextField(
        null=True, blank=True, verbose_name=_('Message for the new users')
    )

    templates_import_data_message = RichTextField(
        null=True, blank=True, verbose_name=_('Template import data message')
    )
    automation_on_data_trigger_message = RichTextField(
        null=True, blank=True,
        verbose_name=_('Automation "On data" trigger message')
    )
    automation_scheduled_trigger_message = RichTextField(
        null=True, blank=True,
        verbose_name=_('Automation "Scheduled" trigger message')
    )
    automation_custom_trigger_message = RichTextField(
        null=True, blank=True,
        verbose_name=_('Automation "Custom" trigger message')
    )

    class Meta:
        verbose_name = _('Site config')
        verbose_name_plural = _('Site config')

    def __str__(self):
        return _('Site config')
