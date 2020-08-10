from contentyze.site_config.models import SiteConfig


def site_config(request):
    return {
        'site_config': SiteConfig.load()
    }
