from modeltranslation.translator import translator, TranslationOptions
from .models import NewsModel, TagsModel


class NewsTranslation(TranslationOptions):
    fields = ('name', 'description',)


class TagsTranslation(TranslationOptions):
    fields = ('tag_name', )


translator.register(NewsModel, NewsTranslation)
translator.register(TagsModel, TagsTranslation)
