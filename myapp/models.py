from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    monotributista = models.BooleanField()
    class Meta: 
        verbose_name_plural = "Profesores"
        verbose_name = "Profesor"
    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField("Nombre", max_length=128)
    inscriptos = models.IntegerField("Inscriptos")
    TURNOS =(
        (1, "Mañana"),
        (2, "Tarde"), 
        (3, "Noche")
    )
    turno = models.PositiveSmallIntegerField("Turno", choices=TURNOS, default=3)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, related_name="cursos")

    def __str__(self):
        return self.nombre
    
class Adidas(models.Model):
    articulo = models.CharField("Articulo", max_length=128)
    talle = models.CharField("Talle", max_length=128)

