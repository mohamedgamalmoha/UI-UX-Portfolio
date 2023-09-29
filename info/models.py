from django.db import models
from django.utils.translation import gettext_lazy as _


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
    title = models.CharField(max_length=500, verbose_name=_("Title"))
    sub_text = models.TextField(verbose_name=_("Sub Text"))
    image = models.ImageField(upload_to='sections/', verbose_name=_('Image'))
    is_active = models.BooleanField(blank=True, null=True, default=True, verbose_name=_('Is Active'),
                                    help_text=_('Determine whether the case study section is going to be displayed on '
                                                'the home page or not.'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))

    objects = ActiveManager()

    class Meta:
        verbose_name = _('Case Study Section')
        verbose_name_plural = _('Case Study Sections')
        ordering = ('-create_at', '-update_at')

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
