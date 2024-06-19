import datetime
# from mptt.models import MPTTModel, TreeForeignKey

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from common.models import Media

from django.db import models
from django.utils.translation import gettext_lazy as _


class Tobacco(models.Model):
    class StrengthChoices(models.TextChoices):
        LIGHT = 'light', _('Light')
        HARD = 'hard', _('Hard')

    class TypeChoices(models.TextChoices):
        MINT = 'mint', _('Mint')
        MIX = 'mix', _('Mix')
        FLAVOR_DRINKS = 'flavor drinks', _('Flavor drinks')
        SPICY = 'spicy', _('Spicy')

    title = models.CharField(_('title'), max_length=120)
    manufacturer = models.ForeignKey('Manufacturer', verbose_name=_("manufacturer"),
                                     on_delete=models.CASCADE)
    leaf = models.CharField(_('leaf'), max_length=120)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name=_("country"),
                                related_name='country')
    composition = models.CharField(_('composition'), max_length=120)
    strength = models.CharField(_('strength'), choices=StrengthChoices.choices, default=StrengthChoices.HARD,
                                max_length=120)
    taste = models.CharField(_('taste'), max_length=120)
    type = models.CharField(_('type'), max_length=120, choices=TypeChoices.choices, default=TypeChoices.MIX)
    tag = models.ManyToManyField('TabaccoTag', verbose_name=_("Tag"), blank=True)
    preparation = models.ManyToManyField('PreMethod', verbose_name=_("preparation"), related_name='tobaccos')
    description = models.TextField(_("description"), max_length=255)

    class Meta:
        verbose_name = _('Tobacco')
        verbose_name_plural = _('Tobaccos')

    def __str__(self):
        return self.title


class TobaccoImages(models.Model):
    photo = models.ForeignKey('common.Media', on_delete=models.CASCADE, verbose_name=_("Photo"))
    tobacco = models.ForeignKey(Tobacco, on_delete=models.CASCADE, verbose_name=_("Tobacco"),
                                related_name="tobacco_images")

    class Meta:
        verbose_name = _('Tobacco Image')
        verbose_name_plural = _('Tobacco Images')

    def __str__(self):
        return f"Image Id: {self.id}| Product: {self.tobacco.title}"


class Manufacturer(models.Model):
    title = models.CharField(_('title'), max_length=120)

    class Meta:
        verbose_name = _('Manufacturer')
        verbose_name_plural = _('Manufacturers')

    def __str__(self):
        return self.title


class Country(models.Model):
    name = models.CharField(_('name'), max_length=120)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return self.name


class TabaccoTag(models.Model):
    title = models.CharField(_('title'), max_length=120)

    class Meta:
        verbose_name = _('TabaccoTag')
        verbose_name_plural = _('TabaccoTags')

    def __str__(self):
        return self.title


class PreMethod(models.Model):
    class PreMethodChoices(models.TextChoices):
        UNWASHED = 'unwashed', _("Unwashed")
        BOILED = 'boiled', _('Boiled')

    title = models.CharField(_("title"), max_length=120, choices=PreMethodChoices.choices,
                             default=PreMethodChoices.BOILED)

    class Meta:
        verbose_name = _('PreMethod')
        verbose_name_plural = _('PreMethods')

    def __str__(self):
        return self.title
