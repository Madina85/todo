from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class ToMeet(models.Model):
    person = models.CharField(max_length=20)
    phone_number = models.PositiveIntegerField(10)
    date_of_meeting = models.DateField('Дата встречи')
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Goal_for_month(models.Model):
    goal = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=100) 
    reason_for_goal = models.CharField(max_length=50)  


    def __str__(self):
            return 'Goal_for_month: {}' .format(self.goal) 