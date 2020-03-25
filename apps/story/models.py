from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.character.models import Character
from apps.location.models import Location, BaseModel, BaseTimeStampModel


class Story(BaseModel):
    class Meta:
        verbose_name = _('Historia')
        verbose_name_plural = _('Historie')

    author = models.ManyToManyField(AUTH_USER_MODEL)


class Event(BaseTimeStampModel):
    class Meta:
        verbose_name = _('Wydarzenie')
        verbose_name_plural = _('Wydarzenia')

    name = models.CharField(verbose_name=_('Nazwa'),
                            default='',
                            max_length=128,
                            null=True,
                            blank=True)
    description = models.TextField(verbose_name=_("Opis"))
    locale = models.ForeignKey(Location,
                               verbose_name=_("Miejsce akcji"),
                               null=True,
                               blank=True,
                               on_delete=models.PROTECT)
    participants = models.ManyToManyField(Character,
                                          verbose_name=_("Uczestnicy wydarzeń"),
                                          blank=True)
    story = models.ForeignKey(Story,
                              verbose_name=_("Historia"),
                              on_delete=models.PROTECT)
    previous_event = models.ForeignKey("self",
                                       verbose_name=_('Poprzednie wydarzenie'),
                                       null=True,
                                       blank=True,
                                       on_delete=models.PROTECT)
    included_in_event = models.ManyToManyField("self",
                                               verbose_name=_('Zawarte w wydarzeniu'),
                                               blank=True)

    def __str__(self):
        return '"{}": {}'.format(self.story.name,
                                 self.description[:64] + "..." if len(self.description) > 64 else self.description)
