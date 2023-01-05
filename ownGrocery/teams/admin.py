from django.contrib import admin

from teams.models import OrgUnit, Worker, Supervisor, WorkerSupervisor

# Register your models here.
 
@admin.register(OrgUnit)
class OrgUnitAdmin(admin.ModelAdmin):
    list_display = ("name", "parent","get_no_children","get_children")
    ordering = ("parent",)
    
    def get_no_children(self, obj):
        no_of_children = OrgUnit.objects.filter(parent=obj).count()
        return no_of_children
    get_no_children.short_description = "No of Children"


    def get_children(self, obj):
        list_of_children = OrgUnit.objects.filter(parent=obj).values_list('name')
        #str_list_children = ','.join(list(list_of_children))
        return list(list_of_children)
    get_children.short_description = "Children"

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("name","company")
    ordering = ("name",)

@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    #list_display = ("employee", "type")
    pass

@admin.register(WorkerSupervisor)
class WorkerSupervisorAdmin(admin.ModelAdmin):
    #list_display = ("employee", "type")
    pass
    
  

