from django.contrib import admin
from AdminApp.models import Category,Cake

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","cat_name")

class CakeAdmin(admin.ModelAdmin):
    list_display=("id","cake_name","price","description","imageurl","category")


admin.site.register(Category,CategoryAdmin)
admin.site.register(Cake,CakeAdmin)
    