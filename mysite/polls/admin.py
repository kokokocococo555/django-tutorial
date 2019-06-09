from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes': ['collapse']}),  # 表示・非表示設定を可能に（デフォルトは非表示）
    ]
    inlines = [ChoiceInline]  # Question編集ページで関連Choiceを編集・追加する
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']  # pub_dateの値で絞り込みできるようにする。フィールドの型に応じた適切なフィルタが設定される
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
