from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

from .enums import LayoutChoices


class ActiveManager(models.Manager):

    def active(self):
        return self.get_queryset().filter(is_active=True)


class CaseStudy(models.Model):
    logo = models.ImageField(upload_to='logos', verbose_name=_('Client Logo'))
    title = models.CharField(max_length=500, verbose_name=_("Title"))
    sub_text = models.TextField(verbose_name=_("Sub Text"))
    image = models.ImageField(upload_to='cases/', verbose_name=_('Image'))
    role = models.TextField(verbose_name=_("Role"))
    collaborators = models.TextField(verbose_name=_("Collaborators"))
    deliverables = models.TextField(verbose_name=_("Deliverables"))
    is_active = models.BooleanField(blank=True, null=True, default=True, verbose_name=_('Is Active'),
                                    help_text=_('Determine whether the case study is going to be displayed on the '
                                                'home page or not.'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))

    objects = ActiveManager()

    class Meta:
        verbose_name = _('Case Study')
        verbose_name_plural = _('Case Studies')
        ordering = ('-create_at', '-update_at')

    def __str__(self):
        return str(self.title)


class CaseStudySection(models.Model):
    case_study = models.ForeignKey(CaseStudy, on_delete=models.CASCADE, related_name='sections')
    number = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_('Number'))
    title = models.CharField(max_length=500, verbose_name=_("Title"))
    sub_text = models.TextField(null=True, blank=True, verbose_name=_("Sub Text"))
    image = models.ImageField(null=True, blank=True, upload_to='sections/', verbose_name=_('Image'))
    layout = models.CharField(max_length=20, choices=LayoutChoices.choices, default=LayoutChoices.CARD,
                              verbose_name=_('Section Layout'))
    is_active = models.BooleanField(blank=True, null=True, default=True, verbose_name=_('Is Active'),
                                    help_text=_('Determine whether the case study section is going to be displayed on '
                                                'the home page or not.'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))

    objects = ActiveManager()

    def save(self, *args, **kwargs):
        if self.layout in (LayoutChoices.IMG_FULL, LayoutChoices.IMG_LEFT, LayoutChoices.IMG_RIGHT) \
                and self.image is None:
            raise ValidationError({
                'image': _(f'Setting layout to {self.layout}, requires a not null image')}
            )
        if self.layout == LayoutChoices.CARD and (self.title is None or self.sub_text is None or self.image is None):
            raise ValidationError({
                'title': _(f'Setting layout to {self.layout}, requires a not null title'),
                'sub_text': _(f'Setting layout to {self.layout}, requires a not null sub text'),
                'image': _(f'Setting layout to {self.layout}, requires a not null image'),
            })
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Case Study Section')
        verbose_name_plural = _('Case Study Sections')
        ordering = ('number', '-create_at', '-update_at')

    def __str__(self):
        return str(self.title)


class DribbleWork(models.Model):
    image = models.ImageField(upload_to='dribbles/', verbose_name=_('Image'))
    url = models.URLField(verbose_name=_('Link'))
    alt = models.CharField(max_length=500, verbose_name=_("Alternative (Alt)"),
                           help_text=_("Text is meant to convey the “why” of the image as it relates to the content of "
                                       "a document or webpage"))
    is_active = models.BooleanField(blank=True, null=True, default=True, verbose_name=_('Is Active'),
                                    help_text=_('Determine whether the dribble work is going to be displayed on the '
                                                'home page or not.'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))

    objects = ActiveManager()

    class Meta:
        verbose_name = _('Dribble Work')
        verbose_name_plural = _('Dribble Works')
        ordering = ('-create_at', '-update_at')

    def __str__(self):
        return str(self.alt)
