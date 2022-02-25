from django.contrib.auth.models import Group
from django.contrib import admin


from .models import *
from rangefilter.filters import DateRangeFilter
from import_export.admin import ImportExportModelAdmin
from .resources import *


admin.site.register(RiskManagerGroup)

@admin.register(SecondData)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ["id", "operator_name", "datetime", "datetime_apply", "datetime_distance","product", "date_credit", "shop", "answer", "manager_username", "discription"]
    list_display_links = ["id", "operator_name", "datetime", "datetime_apply", "datetime_distance", "date_credit", "product", "shop", "answer", "manager_username"]
    list_filter = ("operator_name", ("datetime", DateRangeFilter), "date_credit", "answer", "manager_username","shop")
    exclude = ["status", "step", "front_doc", "back_doc", "card_doc", "datetime_distance", "datetime_apply"]
    search_fields = ["operator_name", "date_credit", "shop", "answer", "manager_username"]
    resource_class = OrderResource

admin.site.register(Operator)
admin.site.register(Shop)
admin.site.register(FirstData)
admin.site.unregister(Group)


