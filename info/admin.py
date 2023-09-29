from django.contrib import admin
from django.contrib.auth.models import Group

from .models import CaseStudy, CaseStudySection, DribbleWork


class CaseStudySectionInlineAdmin(admin.TabularInline):
    model = CaseStudySection
    extra = 1
    min_num = 3
    max_num = None
    can_delete = True
    show_change_link = True


class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'create_at', 'update_at')
    readonly_fields = ('create_at', 'update_at')
    list_filter = ('is_active', )
    search_fields = ('title', 'sub_text', 'role', 'collaborators', 'deliverables')
    inlines = [CaseStudySectionInlineAdmin]


class DribbleWorkAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_active', 'create_at', 'update_at')
    readonly_fields = ('create_at', 'update_at')
    list_filter = ('is_active', )
    search_fields = ('alt', )


admin.site.register(CaseStudy, CaseStudyAdmin)
admin.site.register(DribbleWork, DribbleWorkAdmin)
admin.site.unregister(Group)
