from typing import Union

from django.db import models

from django.utils.translation import ugettext_lazy as _


class BaseNameModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(verbose_name=_('Nazwa'),
                            max_length=128)
    description = models.TextField(verbose_name=_("Opis"),
                                   null=True,
                                   blank=True)

    def __str__(self):
        return self.name


class BaseTimeStampModel(models.Model):
    class Meta:
        abstract = True

    create_date = models.DateTimeField(verbose_name=_('Data stworzenie'),
                                       auto_now_add=True)
    change_date = models.DateTimeField(verbose_name=_('Data ostatniej aktualizacji'),
                                       auto_now=True)


class BaseModel(BaseNameModel, BaseTimeStampModel):
    class Meta:
        abstract = True


class LocationType(BaseNameModel):
    class Meta:
        verbose_name = _('Typ lokacji')
        verbose_name_plural = _('Typy lokacji')


class Location(BaseModel):
    class Meta:
        verbose_name = _('Lokacja')
        verbose_name_plural = _('Lokacje')

    type = models.ForeignKey(LocationType,
                             verbose_name=_("Typ lokacji"),
                             null=False,
                             blank=False,
                             on_delete=models.PROTECT)
    located_in = models.ForeignKey("self",
                                   verbose_name=_('Położony w'),
                                   null=True,
                                   blank=True,
                                   on_delete=models.PROTECT)

    @classmethod
    def get_by_type(cls, location_type: Union[LocationType, str]):
        if type(location_type) is str:
            return cls.objects.filter(type__name=location_type)
        return cls.objects.filter(type=location_type)

    def surrounding_location(self):
        return Location.objects.filter(located_in=self.located_in)

    def contained_location(self):
        return Location.objects.filter(located_in=self)
