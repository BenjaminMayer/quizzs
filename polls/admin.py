from django.contrib import admin
from .models import Quizz, Question, Reponse, Question_value,Quizz_value,Historic
# Register your models here.
admin.site.register(Quizz)
admin.site.register(Question)
admin.site.register(Reponse)
admin.site.register(Question_value)
admin.site.register(Quizz_value)
admin.site.register(Historic)