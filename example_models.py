from django.contrib.auth import get_user_model
from django.db import models
from model_utils.models import TimeStampedModel


User = get_user_model()


class CallModelLog(TimeStampedModel):

    SOURCE_EDITOR = 1
    SOURCE_BULK_WRITER = 2
    SOURCE_TEMPLATES = 3
    SOURCE_AUTOMATION = 4
    SOURCE_API = 5

    SOURCES = (
        (SOURCE_EDITOR, 'Editor'),
        (SOURCE_BULK_WRITER, 'Bulk writer'),
        (SOURCE_TEMPLATES, 'Templates'),
        (SOURCE_AUTOMATION, 'Automation'),
        (SOURCE_API, 'API'),
    )

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, verbose_name='User'
    )
    username = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='User'
    )
    model_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Model name'
    )
    content = models.TextField(
        null=True, blank=True, verbose_name='Content'
    )
    source = models.IntegerField(choices=SOURCES, default=SOURCE_EDITOR)
    params = models.TextField(null=True, blank=True, verbose_name='Params')

    class Meta:
        ordering = ['-modified']


class Weapon(models.Model):

    name = models.CharField(max_length=255, verbose_name=_('Название'))
    img = ImageField(upload_to='weapon')
    base_img = ImageField(upload_to='weapon')
    width = models.IntegerField(verbose_name=_('Ширина'))
    height = models.IntegerField(verbose_name=_('Высота'))
    points = models.ManyToManyField(
        'Point', through='PointWeapon',
        through_fields=('weapon', 'point'), verbose_name=_('Точки')
    )

    def __str__(self):
        return self.name


class PointWeapon(models.Model):

    weapon = models.ForeignKey(Weapon, verbose_name=_('Оружие'))
    point = models.ForeignKey(Point, verbose_name=_('Точка'))
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    is_float = models.BooleanField(default=False, verbose_name=_('Плавающая'))
    x2 = models.IntegerField(blank=True, null=True)
    y2 = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(
        blank=True, null=True, verbose_name=_('Ширина плавающая'))

    class Meta:
        verbose_name = _('Точка оружия')
        verbose_name_plural = _('Точки оружия')

    def __str__(self):
        return f'{self.weapon} - {self.point}'
