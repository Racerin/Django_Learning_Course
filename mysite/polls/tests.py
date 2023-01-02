import datetime, time

from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import *

# Create your tests here.
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_new_question(self):
        """ 
        method .was_published_recently() returns True for questions whose pub_date
        is within one day.
        """
        new_time = timezone.now() - datetime.timedelta(hours=23)
        new_question = Question(pub_date=new_time)
        self.assertIs(new_question.was_published_recently(), True)
        now_question = Question(pub_date=timezone.now())
        time.sleep(1e-6)
        self.assertIs(now_question.was_published_recently(), True)

    def test_was_published_recently_with_old_question(self):
        """ 
        method .was_published_recently() returns False for questions whose pub_date
        is not within 1 day.
        """
        old_times = [timezone.now() - datetime.timedelta(hours=hr_dt) for hr_dt in (25, 48, 24*30, 24*365, 24*1e3)]
        for dt in old_times:
            old_question = Question(pub_date=dt, question_text=str(dt))
            time.sleep(1e-6)
            self.assertIs(old_question.was_published_recently(), False, str(old_question))

    def test_was_published_recently_with_future_question(self):
        """ 
        method was_published_recently() returns Validation Error for questions whose
        pub_date is in the future.
        """
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)
        self.assertRaises(ValidationError, future_question.was_published_recently)
        # self.assertIs(future_question.was_published_recently(), False)
