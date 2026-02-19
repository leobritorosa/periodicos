from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    lattes = models.URLField(verbose_name="Link do Lattes")
    grande_area = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    producao_biblio = models.IntegerField(blank=True, null=True)
    periodico = models.IntegerField(blank=True, null=True)
    livros = models.IntegerField(blank=True, null=True)
    capitulos = models.IntegerField(blank=True, null=True)
    congresso = models.IntegerField(blank=True, null=True)
    resumos = models.IntegerField(blank=True, null=True)
    aceitos = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.nome

class Publicacao(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='publicacoes')
    titulo = models.TextField()
    ano = models.IntegerField()
    link = models.URLField()
    visualizacoes = models.IntegerField()

    def __str__(self):
        return f"{self.titulo}"