import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

__all__ = ['Question', 'Choice', 'timezone', 'datetime']

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(
        max_length=200, 
        unique=True,
        validators=[
            MinValueValidator(3),
            ], 
        )
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{}. {}".format(self.id, self.question_text)

    def was_published_recently(self):
        """ Confirms that published date of question is within 1 day. """
        if self.pub_date >= timezone.now():
            raise ValidationError("{} is a future date to now ({}). Please ensure that the database time is consistent.".format(self.pub_date, timezone.now()))
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(
        max_length=200, 
        validators=[
            MinValueValidator(3),
            ],
        )
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{}. Question {} | {}".format(self.id, self.question, self.choice_text)