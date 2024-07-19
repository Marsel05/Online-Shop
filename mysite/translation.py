from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)