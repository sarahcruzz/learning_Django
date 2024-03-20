import datetime
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) # criando o campo de fazer a pergunta e limitando a quantidade de caracteres da pergunta
    pub_date = models.DateTimeField('date published') # criando o campo de data da publicação que vai registrar quando a pergunta foi feita
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= datetime.timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # toda alternativa tem que estar vinculada a uma pergunta, o foreign Key esta fazendo essa relação entre questão/alternativa
    choice_text = models.CharField(max_length=200) # quais são os textos da alternativa
    votes = models.IntegerField(default=0) # vai ser uma variável que vai guardar
    
    def __str__(self):
        return self.choice_text
    
    
    