from django.contrib import admin
from .models import Company, Education, Work, Portfolio


# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)


class EducationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Education, EducationAdmin)


class WorkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Work, WorkAdmin)


class PortfolioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Portfolio, PortfolioAdmin)
