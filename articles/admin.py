from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def save(self):
        count_main = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count_main += 1

        if count_main > 1:
            raise ValidationError('Может быть только один основной раздел!')

        return super().save()


class ScopeInline(admin.TabularInline):
    model = Article.tags.through
    extra = 0
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
