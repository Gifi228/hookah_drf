from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import Media
from lounge.utils import validate_phone_number


class Lounge(models.Model):
    metro = models.ForeignKey('Metro', on_delete=models.CASCADE, verbose_name=_("Metro"), related_name='metro')
    title = models.CharField(_('Title'), max_length=120)
    price = models.CharField(_('Price'), max_length=120)
    rate_google = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], verbose_name='Рейтинг Google')
    rate_yandex = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], verbose_name='Рейтинг Yandex')
    phone_number = models.CharField(_("phone number"), max_length=20,
                                    validators=[validate_phone_number])
    work_time = models.DateTimeField(_("work time"))
    description = models.TextField(_("description"), max_length=255)

    class Meta:
        verbose_name = "Lounge"
        verbose_name_plural = "Lounges"

    def __str__(self):
        return f"{self.title}"


class SocialMedia(models.Model):
    title_choices = (
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('Twitter', 'Twitter'),
        ('YouTube', 'YouTube'),
    )

    lounge = models.ForeignKey(Lounge, on_delete=models.CASCADE)
    title = models.CharField(choices=title_choices, max_length=50)
    url = models.URLField()

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"

    def __str__(self):
        return f"{self.title} - {self.lounge}"


class LoungeImages(models.Model):
    photo = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_("photo"))
    lounge = models.ForeignKey(Lounge, on_delete=models.CASCADE, verbose_name=_("lounge"),
                               related_name='lounge_images')

    class Meta:
        verbose_name = "Lounge Images"
        verbose_name_plural = "Lounge Images"


class Metro(models.Model):
    title = models.CharField(_('Title'), max_length=120)


    class Meta:
        verbose_name = "Metro"
        verbose_name_plural = "Metro"

    def __str__(self):
        return f"{self.title}"
