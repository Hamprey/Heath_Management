from django.db import models


class HealthProgram(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.PositiveIntegerField(default=18)
    email = models.EmailField(default="example@example.com", unique=True)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        names = filter(None, [self.first_name, self.middle_name, self.last_name])
        return " ".join(names)


class Enrollment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    program = models.ForeignKey(HealthProgram, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('client', 'program')  # Optional but good!

    def __str__(self):
        return f"{self.client} -> {self.program}"

