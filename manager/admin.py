from django.contrib import admin
from .models import venu,customer_requests,customer_register
# Register your models here.


class venu_admin(admin.ModelAdmin):
    list_display = ["name","booking_price","nonveg_pricing","veg_pricing","h_drinks"]
    search_fields = ["name"]
    list_filter = ["booking_price","nonveg_pricing","veg_pricing","h_drinks"]

    class Meta:
        model = venu


class request_admin(admin.ModelAdmin):
    list_display = ["date","name","ph_number","email","venue","event_type","status"]
    search_fields = ["name","venue","date","event_type"]
    list_filter = ["date","name","venue","event_type"]

    class Meta:
        model = customer_requests


class register_admin(admin.ModelAdmin):
    list_display = ["f_name","l_name","u_name","email","ph_number","password"]
    search_fields = ["f_name","l_name","email","u_name"]

    class Meta:
        model = customer_register


admin.site.register(venu, venu_admin)
admin.site.register(customer_requests, request_admin)
admin.site.register(customer_register, register_admin)
