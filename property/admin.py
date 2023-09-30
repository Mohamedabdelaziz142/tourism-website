from django.utils import timezone
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (Property,
                      PropertyBook, 
                      PropertyImages, 
                      PropertyReview, 
                      Category,
                      Place,
                      )
# Register your models here.

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name' , 'price' , 'get_avg_rating','check_availability']


admin.site.register(Property, SomeModelAdmin)

class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ['property', 'in_progress']

    def in_progress(self, obj):
        now = timezone.now().date()
        return now > obj.date_from and now < obj.date_to

    in_progress.boolean = True
admin.site.register(PropertyBook, PropertyBookAdmin)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)
admin.site.register(Place)


