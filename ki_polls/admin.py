from django.contrib import admin
from .models import Question,Choice

# Ensure there is only one registration for Bookmark
class QuestionkAdmin(admin.ModelAdmin):
    list_display = ('category','id')

# Register the Bookmark model with its admin configuration
admin.site.register(Question, QuestionkAdmin)

# Ensure there is only one registration for Bookmark
class ChoiceAdmin(admin.ModelAdmin):
    model = Choice
    extra = 10
    list_display = ('name','price')

# Register the Bookmark model with its admin configuration
admin.site.register(Choice, ChoiceAdmin)