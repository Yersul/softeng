from django.contrib import admin

# Register your models here.
from .models import Timee


class ClientDetailsAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super(ClientDetailsAdmin, self).get_changeform_initial_data(request)
        get_data['created_by'] = request.user.pk
        return get_data


admin.site.register(Timee, ClientDetailsAdmin)
