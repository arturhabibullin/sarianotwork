from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Category)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'date_production', 'company', 'product', 'get_categorys', 'bb_for_i', 'bb_and_for', 'pallet_for_i', 'pallet_and_for', 'repeate', 'date_reg', 'comment')
    ordering = ['-date_reg']
    def get_categorys(self, obj):
        return "\n".join([p.categorys for p in obj.category.all()])
    
admin.site.register(Sample, SampleAdmin)

# # admin.site.register(Bruker)
class FatAdmin(admin.ModelAdmin):
    list_display = ('samples', 'fat_blank_cup', 'fat_sample_mass', 'fat', 'date_pub')

admin.site.register(Fat, FatAdmin)


# class ProteinAdmin(admin.ModelAdmin):
#     list_display = ('samples', 'sample_mass', 'titrant_volume', 'protein', 'date_pub')

# admin.site.register(Protein, ProteinAdmin)

