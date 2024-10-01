from django.contrib import admin

from questions.models import Categories
from questions.models import Questions

#admin.site.register(Categories)
#admin.site.register(Questions)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
    