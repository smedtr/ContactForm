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
        return list(list_of_children)
    get_children.short_description = "Children"

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("name","company","get_supervisor")       
    ordering = ("name",)

    def get_supervisor(self, obj):
        get_supervisor = WorkerSupervisor.objects.filter(worker=obj.id).values_list('supervisor__employee__name')        
        return list(get_supervisor)
    get_supervisor.short_description = "Supervisor"

@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):  
    list_display = ("employee","get_supervisor_company","get_supervised_team") 
    ordering = ("employee",)
    
    def get_supervisor_company(self, obj):
        get_supervisor_company = Worker.objects.filter(id=obj.employee.id).values_list('company')              
        return list(get_supervisor_company)
    get_supervisor_company.short_description = "Company"   
    
    def get_supervised_team(self, obj):
        get_supervised_team = WorkerSupervisor.objects.filter(supervisor=obj.id).values_list('worker__name')                
        return list(get_supervised_team)
    get_supervised_team.short_description = "Team"

@admin.register(WorkerSupervisor)
class WorkerSupervisorAdmin(admin.ModelAdmin):
    list_display = ("worker", "type","supervisor")
    ordering = ("worker",)
    
    
  

