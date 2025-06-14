from django.contrib import admin



# Register your models here.

from . models import Categorys,Product

#admin.site.register(Categorys)
#admin.site.register(Product)

@admin.register(Categorys)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class productAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}

