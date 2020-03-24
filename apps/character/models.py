from typing import Union

from django.contrib.postgres.fields import JSONField
from django.db import models

from django.utils.translation import ugettext_lazy as _

from apps.location.models import Location, BaseNameModel, BaseModel, BaseTimeStampModel


class AttributeType(BaseNameModel):
    class Meta:
        verbose_name = _('Typ Atrybutu')
        verbose_name_plural = _('Typy Atrybutu')


class Attribute(BaseModel):
    class Meta:
        verbose_name = _('Atrybut')
        verbose_name_plural = _('Atrybuty')

    type = models.ForeignKey(AttributeType,
                             verbose_name=_("Typ Atrybutu"),
                             null=False,
                             blank=False,
                             on_delete=models.PROTECT)

    def __str__(self):
        return "{}: {}".format(self.type.name, self.name)

    @classmethod
    def get_by_type(cls, location_type: Union[AttributeType, str]):
        if type(location_type) is str:
            return cls.objects.filter(type__name=location_type)
        return cls.objects.filter(type=location_type)


class Character(BaseTimeStampModel):
    class Meta:
        verbose_name = _('Postać')
        verbose_name_plural = _('Postacie')

    name = models.CharField(verbose_name=_('Imie'),
                            max_length=128)
    second_names = JSONField(verbose_name=_('Kolejne imion'),
                             default=list,
                             null=True,
                             blank=True)
    surname = models.CharField(verbose_name=_('Nazwisko'),
                               max_length=128,
                               null=True,
                               blank=True)
    second_surnames = JSONField(verbose_name=_('Kolejne nazwiska'),
                                default=list,
                                null=True,
                                blank=True)
    description = models.TextField(verbose_name=_("Opis profesji"))
    attribute = models.ManyToManyField(Attribute,
                                       verbose_name=_('Atrybut'),
                                       blank=True)
    provenience = models.ForeignKey(Location,
                                    on_delete=models.PROTECT,
                                    verbose_name=_("Pochodzenie"),
                                    null=True,
                                    blank=True)

    def __str__(self):
        return self.name
