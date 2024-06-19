from django.db import models
from django.utils.translation import gettext_lazy as _
from tobacco.models import Tobacco


class MixCategory(models.Model):
    title = models.CharField(_("title"), max_length=120)

    class Meta:
        verbose_name = _("mix category")
        verbose_name_plural = _("mix categories")

    def __str__(self):
        return self.title


class Mix(models.Model):
    title = models.CharField(_("title"), max_length=120)
    description = models.TextField()
    tags = models.ManyToManyField('MixTag', verbose_name=_("tags"), blank=True)
    variants = models.ManyToManyField("Variant", verbose_name=_("variants"), blank=True)
    category = models.ForeignKey(MixCategory, verbose_name=_("category"),
                                 on_delete=models.CASCADE)
    strength = models.ForeignKey('Strength', on_delete=models.CASCADE, verbose_name=_("strength"),
                                 related_name='strength')

    class Meta:
        verbose_name = _("mix")
        verbose_name_plural = _("mixes")

    def __str__(self):
        return self.title


class MixTag(models.Model):
    title = models.CharField(_("title"), max_length=120)

    class Meta:
        verbose_name = _("mix tag")
        verbose_name_plural = _("mix tags")

    def __str__(self):
        return self.title


class Variant(models.Model):
    title = models.CharField(_("title"), max_length=120)

    class Meta:
        verbose_name = _("variant")
        verbose_name_plural = _("variants")

    def __str__(self):
        return self.title


class Strength(models.Model):
    mix = models.ForeignKey(Mix, on_delete=models.CASCADE,
                            verbose_name=_("mix"), related_name='strengths')
    tobacco = models.ForeignKey(Tobacco, on_delete=models.CASCADE,
                                verbose_name=_("tobacco"), related_name='strengths')
    percentage = models.IntegerField(_("percentage"), )
