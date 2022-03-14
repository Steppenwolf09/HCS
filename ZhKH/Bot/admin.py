from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    class Meta:
        model=News

admin.site.register(News, NewsAdmin)


class StatusAdmin(admin.ModelAdmin):
    class Meta:
        model=Status

admin.site.register(Status,StatusAdmin)



class ProposalAdmin(admin.ModelAdmin):
    class Meta:
        model=Proposal

admin.site.register(Proposal,ProposalAdmin)


class AdmissionAdmin(admin.ModelAdmin):
    class Meta:
        model = Admission

admin.site.register(Admission, AdmissionAdmin)

class EmployeeTypeAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeType

admin.site.register(EmployeeType, EmployeeTypeAdmin)

class EmployeeCallingAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeCalling

admin.site.register(EmployeeCalling, EmployeeCallingAdmin)

class ContactsAdmin(admin.ModelAdmin):
    class Meta:
        model = Contacts

admin.site.register(Contacts, ContactsAdmin)

