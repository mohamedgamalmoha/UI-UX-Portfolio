from django.db import models
from django.utils.translation import gettext_lazy as _


class LayoutChoices(models.TextChoices):
    IMG_FULL = 'img-full', _('Image Full Width')
    IMG_LEFT = 'img-left', _('Image ON Right')
    IMG_RIGHT = 'img-right', _('Image ON Left')
    CARD = 'card', _('Card')
    QUOTE = 'quote', _('Quote')
    TEXT_ONLY = 'text', _('Text only')
