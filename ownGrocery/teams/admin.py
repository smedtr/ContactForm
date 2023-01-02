from django.contrib import admin
from teams.models import OrgUnit

# Register your models here.
 
@admin.register(OrgUnit)
class OrgUnit(admin.ModelAdmin):
    list_display = ("name", "type", "parent", )
    ordering = ("name",)

    #def get_no_parents(self, obj):
    #    no_of_parents = OrgUnit.parent.filter(parent=obj).count()
    #    return no_of_parents
    #get_no_parents.short_description = "No of Parents"

