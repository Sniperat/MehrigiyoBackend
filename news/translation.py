from modeltranslation.translator import translator, TranslationOptions
from .models import NewsModel


class NewsTranslation(TranslationOptions):
    fields = ('name', 'description',)


translator.register(NewsModel, NewsTranslation)
