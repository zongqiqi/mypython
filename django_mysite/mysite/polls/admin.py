from django.contrib import admin

from .models import Question,Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
	model=Choice
	extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines=[ChoiceInline]#关联数据
    list_display=("question_text","pub_date","was_published_recently")#显示信息 
    list_filter=['pub_date']#提供数据过滤
    search_fields=['question_text']

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)