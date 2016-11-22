from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django_countries.fields import CountryField
# Create your models here.


class Sin(models.Model):
    UNISEX = 'US'
    MALE = 'M'
    FEMALE = 'F'
    GAY_MALE = 'GM'
    GAY_FEMALE = 'GF'
    TRANS_MALE = 'TM'
    TRANS_FEMALE = 'TF'

    LANGUAGE_CHOICES = settings.LANGUAGES

    TARGET_SEX = (
        (UNISEX, _('Unisex')),
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    )

    text = models.CharField(max_length=255)
    cost = models.IntegerField(default=1)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, default=settings.LANGUAGE_CODE)
    target_sex = models.CharField(choices=TARGET_SEX, default=UNISEX, max_length=2)
    sinners = models.ManyToManyField(Sinner)


class Sinner(models.Model):
    UNISEX = 'US'
    MALE = 'M'
    FEMALE = 'F'
    TARGET_SEX = (
        (UNISEX, _('Unisex')),
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    )

    ATHEISM = 'AT'
    CHRISTIANITY = 'CR'
    ISLAM = 'IS'
    HINDUISM = 'HI'
    BUDDHISM = 'BU'
    SIKHISM = "SK"
    JUDAISM = "JI"
    BAHAISM = "BA"
    CONFUCIANISM = "CO"
    JAINISM = "JA"
    SHINTOISM = "SN"
    
    RELIGION_CHOICES = (
        (ATHEISM, _('Atheism')),
        (CHRISTIANITY, _('Christianity')),
        (ISLAM, _("Islam")),
        (HINDUISM, _("Hinduism")),
        (BUDDHISM, _('Buddhism')),
        (SIKHISM, _("Sikhism")),
        (JUDAISM, _("Judaism")),
        (BAHAISM, _("Bahaism")),
        (CONFUCIANISM, _("Confucianism")),
        (JAINISM, _("Jainism")),
        (SHINTOISM, _("Shintoism"))
    )

    age = models.PositiveIntegerField(default=16)
    sex = models.CharField(choices=TARGET_SEX, default=UNISEX, max_length=2)
    occupation = models.CharField(max_length=255)
    country_of_residence = CountryField(blank_label=_('(select country)'))
    religion = models.CharField(max_length=2, choices=RELIGION_CHOICES, default=ATHEISM)

