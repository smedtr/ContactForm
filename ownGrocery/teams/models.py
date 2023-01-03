from django.db import models
from datetime import date 

# Create your models here.

# OrgUnit, Employee, Organisation
class OrgUnit(models.Model):
    # CHOICES
    HIERARCHICAL = 'HI'
    FUNCTIONAL = 'FU'
    TYPE_ORG_UNIT = (
        (HIERARCHICAL, 'Hierarchical Unit'),
        (FUNCTIONAL, 'Functional Unit'),       
    )

    # DATABASE FIELDS
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name=('parent'),
        related_name='children',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=2,choices=TYPE_ORG_UNIT, db_index=True)
    is_active = models.BooleanField(default=True)    
    starting_at = models.DateField(default=date.today, null=True, blank=True)    
    ending_at = models.DateField(null=True, blank=True)

    # META CLASS
    class Meta:
        verbose_name = 'org_unit'
        verbose_name_plural = 'org_units'

    def __str__(self):
        return self.name

    # Verschil tussen call method en property ? by de def komt er dan @propert te staan


class Worker(models.Model):
    # DATABASE FIELDS
    # CHOICES
    KYNDRYL_BE = 'KYND-BE'
    KYNDRYL_CIC_PL = 'CIC-PL'
    PI_SQUARE = 'PISQ-BE'
    COMPANY_CODE = (
        (KYNDRYL_BE, 'Kyndryl BE'),
        (PI_SQUARE, 'PI-SQUARE'),       
    )
    manager = models.ForeignKey(
        'Supervisor',
        on_delete=models.CASCADE,
        verbose_name=('manager'),
        related_name='worker',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.CharField(max_length=7,choices=COMPANY_CODE, db_index=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)    
    is_active = models.BooleanField(default=True)    
    starting_at = models.DateField(default=date.today, null=True, blank=True)    
    ending_at = models.DateField(null=True, blank=True)

    # META CLASS
    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    def __str__(self):
        return self.name
   
class Supervisor(models.Model):
    # CHOICES
    HIERARCHICAL = 'HI'
    FUNCTIONAL = 'FU'
    TYPE_SUPERVISOR_ROLE = (
        (HIERARCHICAL, 'Hierarchical Manager'),
        (FUNCTIONAL, 'Functional Manager'),       
    )
    employee = models.ForeignKey(
        'Worker',
        on_delete=models.CASCADE,
        verbose_name=('employee'),
        related_name='supervisor',
        blank=True,
        null=True,
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=2,choices=TYPE_SUPERVISOR_ROLE, db_index=True)
    description = models.TextField(null=True, blank=True)    
    is_active = models.BooleanField(default=True)    
    starting_at = models.DateField(default=date.today, null=True, blank=True)    
    ending_at = models.DateField(null=True, blank=True)

    # META CLASS
    class Meta:
        verbose_name = 'supervisor'
        verbose_name_plural = 'supervisors'

    def __str__(self):
        return self.employee.name
    