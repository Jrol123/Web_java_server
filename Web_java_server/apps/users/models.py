from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

c = Question(question_text="loh", pub_date="2022-11-22")
c.save()
