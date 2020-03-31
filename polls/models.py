from django.db import models
from django.utils import timezone
# Create your models here.




class Question(models.Model):
    question = models.CharField(max_length=400)
    reponseA = models.CharField(max_length=400)
    reponseB = models.CharField(max_length=400)
    reponseC = models.CharField(max_length=400)
    reponseD = models.CharField(max_length=400)
    choice = (
        ('A','A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    bonneReponse = models.TextField(choices=choice)
    pireReponse = models.TextField(choices=choice)

    def __str__(self):
        return self.question



class Quizz(models.Model):
    nomDuQuizz = models.CharField(max_length=400,null=True)
    questions = models.ManyToManyField(Question)
    def __str__(self):
        return self.nomDuQuizz
class Reponse(models.Model):
    choice = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    reponse_choisie = models.TextField(choices=choice)
    question_coresponddante = models.ForeignKey(Question,on_delete=models.CASCADE)
    score = models.IntegerField(null=True,blank=True)

    def save(self, *args, **kwargs):
        question = Question.objects.get(question=self.question_coresponddante)
        if question.bonneReponse == self.reponse_choisie:
            self.score = 2
        elif question.pireReponse == self.reponse_choisie:
            self.score = 0
        else:
            self.score = 1
        super(Reponse, self).save(*args, **kwargs)




class Question_value(models.Model):
    question = models.CharField(max_length=400)
    reponseA = models.CharField(max_length=400)
    reponseB = models.CharField(max_length=400)
    reponseC = models.CharField(max_length=400)
    reponseD = models.CharField(max_length=400)
    choice = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    caracteristic_value_1 = models.TextField(choices=choice,blank=False)
    caracteristic_value_2 = models.TextField(choices=choice,blank=False)
    caracteristic_value_3 = models.TextField(choices=choice,blank=False)
    caracteristic_value_4 = models.TextField(choices=choice,blank=False)

    def __str__(self):
        return self.question
class Quizz_value(models.Model):
    nomDuQuizz = models.TextField(null=True,blank=True)
    questions = models.ManyToManyField(Question_value)
    caracteristic_value_1_name = models.CharField(max_length=400)
    caracteristic_value_2_name = models.CharField(max_length=400)
    caracteristic_value_3_name = models.CharField(max_length=400)
    caracteristic_value_4_name = models.CharField(max_length=400)
    def __str__(self):
        return self.nomDuQuizz
class Reponse_value(models.Model):
    choice = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    reponse_choisie = models.TextField(choices=choice)
    question_coresponddante = models.ForeignKey(Question_value,on_delete=models.CASCADE)
    score_value_1 = models.IntegerField(null=True,blank=True)
    score_value_2 = models.IntegerField(null=True, blank=True)
    score_value_3 = models.IntegerField(null=True, blank=True)
    score_value_4 = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        question = Question_value.objects.get(question=self.question_coresponddante)
        if question.caracteristic_value_1 == self.reponse_choisie:
            self.score_value_1 = 1
            self.score_value_2 = 0
            self.score_value_3 = 0
            self.score_value_4 = 0
        elif question.caracteristic_value_2 == self.reponse_choisie:
            self.score_value_1 = 0
            self.score_value_2 = 1
            self.score_value_3 = 0
            self.score_value_4 = 0
        elif question.caracteristic_value_3 == self.reponse_choisie:
            self.score_value_1 = 0
            self.score_value_2 = 0
            self.score_value_3 = 1
            self.score_value_4 = 0
        elif question.caracteristic_value_4 == self.reponse_choisie:
            self.score_value_1 = 0
            self.score_value_2 = 0
            self.score_value_3 = 0
            self.score_value_4 = 1

        super(Reponse, self).save(*args, **kwargs)

class Historic(models.Model):
    quizz_id = models.ForeignKey(Quizz,on_delete=models.CASCADE,null=True)
    quizz_value_id = models.ForeignKey(Quizz_value,on_delete=models.CASCADE,null=True)
    score = models.IntegerField()
    user_id = models.IntegerField()
    date = models.TimeField(default=timezone.now())