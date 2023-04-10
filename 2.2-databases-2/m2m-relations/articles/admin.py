from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope


class ScopeInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        primary_tag_count = len([
            True for form in self.forms
            if form.cleaned_data.get('is_main') and not
            form.cleaned_data.get('DELETE')
        ])
        if primary_tag_count < 1:
            raise ValidationError('Укажите основной раздел')
        elif primary_tag_count > 1:
            raise ValidationError('Можно указать только один основной раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['title', 'text', 'published_at', 'image']
