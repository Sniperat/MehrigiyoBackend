from django.db import models
import datetime
# from django.utils.translation import gettext as _

today = datetime.date.today()


class NewsModel(models.Model):
    image = models.ImageField(upload_to=f'news/{today.year}-{today.month}-{today.month}/',
                              null=True, blank=True)
    name = models.CharField(max_length=255)
    hashtag = models.ForeignKey('TagsModel', on_delete=models.RESTRICT)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TagsModel(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

    # def get_news(self):
    #     return NewsModel.objects.filter(hashtag__tag_name=self.tag_name)
