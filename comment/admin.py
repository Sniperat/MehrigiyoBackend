from django.contrib import admin
from comment.models import CommentDoctor, CommentMedicine


admin.site.register(CommentDoctor)
admin.site.register(CommentMedicine)
