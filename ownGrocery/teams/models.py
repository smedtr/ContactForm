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

    