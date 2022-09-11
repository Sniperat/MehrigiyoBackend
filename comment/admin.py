from django.contrib import admin
from comment.models import CommentDoctor, CommentMedicine, QuestionsModel


admin.site.register(CommentDoctor)
admin.site.register(CommentMedicine)
admin.site.register(QuestionsModel)
