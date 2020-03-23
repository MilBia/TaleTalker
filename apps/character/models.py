from django.db import models

from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(verbose_name=_('Nazwa'),
                            max_length=128)
    description = models.TextField(verbose_name=_("Opis"))

    def __str__(self):
        return self.name


class BaseTimeStampModel(models.Model):
    class Meta:
        abstract = True

    create_date = models.DateTimeField(verbose_name=_('Data stworzenie'),
                                       auto_now_add=True)
    change_date = models.DateTimeField(verbose_name=_('Data ostatniej aktualizacji'),
                                       auto_now=True)


class AttributeType(BaseModel):
    class Meta:
        verbose_name = _('Typ Atrybutu')
        verbose_name_plural = _('Typy Atrybutu')


class Attribute(BaseModel, BaseTimeStampModel):
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


class Character(BaseTimeStampModel):
    class Meta:
        verbose_name = _('Postać')
        verbose_name_plural = _('Postacie')

    name = models.CharField(verbose_name=_('Imie'),
                            max_length=128)
    description = models.TextField(verbose_name=_("Opis profesji"))
    attribute = models.ManyToManyField(Attribute,
                                       verbose_name=_('Atrybut'),
                                       null=True,
                                       blank=True)

    def __str__(self):
        return self.name
