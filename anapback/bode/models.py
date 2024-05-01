from django.db import models

class Orcamento(models.Model):
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.CharField(max_length=255, default='Cliente')

    def __str__(self):
        return f"Orcamento(id={self.id})"

class Material(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Movel(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class PecaAvulsaPadrao(models.Model):
    nome = models.CharField(max_length=255)
    altura = models.FloatField()
    largura = models.FloatField()
    espessura = models.FloatField()

    def __str__(self):
        return f"PecaAvulsaPadrao(nome={self.nome}, altura={self.altura}, largura={self.largura})"

class PecaAvulsa(models.Model):
    nome = models.CharField(max_length=255)
    altura = models.FloatField()
    largura = models.FloatField()
    espessura = models.FloatField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    movel = models.ForeignKey(Movel, on_delete=models.CASCADE)

    def __str__(self):
        return f"PecaAvulsa(nome={self.nome}, altura={self.altura}, largura={self.largura}, espessura={self.espessura}, preco={self.preco}, material={self.material})"


    

