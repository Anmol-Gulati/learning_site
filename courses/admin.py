from django.contrib import admin
from datetime import date

from . import models


def make_published(modeladmin, request, queryset):
	queryset.update(status='p', published=True)

make_published.short_description = 'Mark selected  courses as Publishded' 


class AnswerInline(admin.TabularInline):
	model = models.Answer


class TextInline(admin.StackedInline):
	model = models.Text


class YearListFilter(admin.SimpleListFilter):
	title = 'year created'

	parameter_name = 'year'

	def lookups(self, request, model_admin):
		return (
			('2015', '2015'),
			('2016', '2016'),
		)

	def queryset(self, request, queryset):
		if self.value() == '2015':
			return queryset.filter(created_at__gte=date(2015, 1, 1),
								   created_at__lte=date(2015, 12, 31))

		if self.value() == '2016':
			return queryset.filter(created_at__gte=date(2016, 1, 1),
								   created_at__lte=date(2016, 12, 31))						   		


class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInline,]

	search_fields = ['prompt']

	list_display = ['prompt', 'quiz', 'order']

	list_editable = ['quiz', 'order']

	radio_fields = {'quiz': admin.HORIZONTAL}


class QuizAdmin(admin.ModelAdmin):
	fields = ['course', 'title', 'description', 'order', 'total_questions']


class CourseAdmin(admin.ModelAdmin):
	inlines = [TextInline,]

	search_fields = ['title', 'description']

	list_filter = ['created_at', 'published', YearListFilter]

	list_display = ['title', 'created_at', 'published', 'time_to_complete', 'status']

	list_editable = ['status']

	actions = [make_published]


class TextAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {'fields': ('course', 'title', 'order', 'description')}),
		('Add Content', {'fields': ('content', ), 'classes': ('collapse',)})
	)		

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Text, TextAdmin)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.MultipleChoiceQuestion, QuestionAdmin)
admin.site.register(models.TrueFalseQuestion, QuestionAdmin)
admin.site.register(models.Answer)