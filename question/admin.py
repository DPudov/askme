from django.contrib import admin

from question.models import Answer
from question.models import LikeAnswer
from question.models import LikeQuestion
from question.models import Question
from question.models import Tag
# Register your models here.
from question.models import User

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(LikeAnswer)
admin.site.register(LikeQuestion)