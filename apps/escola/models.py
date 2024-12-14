from django.db import models

class Estudante(models.Model):
    nome = models.CharField(verbose_name='qual o nome', max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    data_nascimento = models.DateField()
    numero = models.CharField(max_length=14, blank=False, null=False)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    )
    codigo = models.CharField(max_length=10, blank=False, null=False)
    descricao = models.TextField(verbose_name='qual a descrição', blank=False, null=False)
    nivel = models.CharField(max_length=1, choices=NIVEL, default='B', blank=False, null=False)
        
    def __str__(self):
        return self.codigo

class Matricula(models.Model):
    PERIODO = (
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, default='M', blank=False, null=False)
