from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from example.site_config.models import SiteConfig


class SingletonAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        if self.model.objects.all().count() == 1:
            obj = self.model.objects.first()
            obj_url = 'admin:{0}_{1}_change'.format(
                self.model._meta.app_label, self.model._meta.model_name
            )
            return HttpResponseRedirect(reverse(obj_url, args=(obj.id,)))
        return super().changelist_view(
            request=request, extra_context=extra_context)


@admin.register(SiteConfig)
class SiteConfigAdmin(SingletonAdmin):

    list_display = ('__str__', )

    fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': (
                'user_message',
            )
        }),
        ('Templates page', {
            'classes': ('wide'),
            'fields': (
                'templates_import_data_message',
            )
        }),
        ('Automation page', {
            'classes': ('wide'),
            'fields': (
                'automation_on_data_trigger_message',
                'automation_scheduled_trigger_message',
                'automation_custom_trigger_message'
            )
        }),
    )
