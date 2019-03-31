from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(models.Manager):
    def create_user(self, username, email, password):
        user = self.create(username=username, email=email, password=password, upload='static/img/stub.png')
        return user


class TagsManager(models.Manager):
    def create_tag(self, title):
        tag = self.create(title=title)
        return tag


class QuestionManager(models.Manager):
    def create_question(self, author, title, test, create_date, is_active):
        question = self.create(author=author, title=title, test=test, create_date=create_date, is_active=is_active)
        return question


class AnswerManager(models.Manager):
    def create_answer(self, author, question, text, create_date):
        answer = self.create(author=author, question=question, text=text, create_date=create_date)
        return answer


# Create your models here.
class User(AbstractUser):
    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/')


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"тег")

    objects = TagsManager()

    def __str__(self):
        return self.title


class LikeAnswer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    isLike = models.BooleanField(default=True, verbose_name=u"Like(true) or dislike(false)")


class LikeQuestion(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    isLike = models.BooleanField(default=True, verbose_name=u"Like(true) or dislike(false)")


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=120, verbose_name=u"Заголовок")
    test = models.TextField(verbose_name=u"Полное описание")

    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Дата создания")

    is_active = models.BooleanField(default=True, verbose_name=u"Активный")

    tags = models.ManyToManyField(Tag, blank=True)

    likes = models.ManyToManyField(LikeQuestion, blank=True)

    objects = QuestionManager()


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    likes = models.ManyToManyField(LikeAnswer, blank=True)

    text = models.TextField(verbose_name=u"Ответ")

    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Дата создания")

    objects = AnswerManager()


class Meta:
    ordering = '-create_date'
