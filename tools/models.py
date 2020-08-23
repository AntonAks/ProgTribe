from django.db import models
from datetime import timedelta, datetime


class Feedback(models.Model):

    feedback_client_id = models.TextField(null=False)
    feedback_name = models.TextField(null=False)
    feedback_email = models.TextField(null=False)
    feedback_time_stamp = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Feedback, self).save(*args, **kwargs)

    def __str__(self):
        return f"id: {self.feedback_client_id}, created at: {self.feedback_time_stamp}"

    def is_older_then_hour(self):

        time_now = datetime.utcnow()
        time_from_db = datetime(year=self.feedback_time_stamp.year,
                                month=self.feedback_time_stamp.month,
                                day=self.feedback_time_stamp.day,
                                hour=self.feedback_time_stamp.hour,
                                minute=self.feedback_time_stamp.minute)

        return time_now - time_from_db > timedelta(hours=1)

    def get_time_left_for_feedback(self):
        time_now = datetime.utcnow()
        time_from_db = datetime(year=self.feedback_time_stamp.year,
                                month=self.feedback_time_stamp.month,
                                day=self.feedback_time_stamp.day,
                                hour=self.feedback_time_stamp.hour,
                                minute=self.feedback_time_stamp.minute)
        time_left_for_feedback = timedelta(hours=1) - (time_now - time_from_db)

        return time_left_for_feedback.seconds // 60


    class Meta:
        verbose_name_plural = 'Feedback Tracker'
