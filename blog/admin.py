from django.contrib import admin
from tof.admin import TofAdmin, TranslationTabularInline
from.models import Post,Category
# Register your models here.

class CategoryAdmin(TofAdmin):
    inlines = (TranslationTabularInline, )




admin.site.register(Post)
admin.site.register(Category,CategoryAdmin)
