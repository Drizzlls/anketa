from django.contrib import admin
from .models import *

class PlaceOfRegistrationForLeadAdmin(admin.ModelAdmin):
    fields = ['region', 'idRegion']
    list_display = ('region', 'idRegion')

class PlaceOfResidenceForLeadAdmin(admin.ModelAdmin):
    fields = ['region', 'idRegion']
    list_display = ('region', 'idRegion')

class PlaceOfRegistrationForDealAdmin(admin.ModelAdmin):
    fields = ['region', 'idRegion']
    list_display = ('region', 'idRegion')

class PlaceOfResidenceForDealAdmin(admin.ModelAdmin):
    fields = ['region', 'idRegion']
    list_display = ('region', 'idRegion')

admin.site.register(PlaceOfRegistrationForLead, PlaceOfRegistrationForLeadAdmin)
admin.site.register(PlaceOfResidenceForLead, PlaceOfResidenceForLeadAdmin)
admin.site.register(PlaceOfRegistrationForDeal, PlaceOfRegistrationForDealAdmin)
admin.site.register(PlaceOfResidenceForDeal, PlaceOfResidenceForDealAdmin)