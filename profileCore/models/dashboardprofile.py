from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin, 
    BaseUserManager
)
from simple_history.models import HistoricalRecords
from django.db import models


class DashboardProfileManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class DashboardProfile(AbstractBaseUser, PermissionsMixin):
    SEX_CHOICES = ((1, "F"), (2, "M"))

    BLOOD_TYPES = (
        (1, "A+"),
        (2, "A-"),
        (3, "B+"),
        (4, "B-"),
        (5, "AB+"),
        (6, "AB-"),
        (7, "O+"),
        (8, "O-"),
    )
    name = models.CharField(max_length=144)
    username = None
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    sex = models.IntegerField(blank=True, null=True, choices=SEX_CHOICES)
    weigth = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=5)
    heigth = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=3)
    emergency_phone_number = models.CharField(blank=True, null=True, max_length=10)
    blood_type = models.IntegerField(blank=True, null=True, choices=BLOOD_TYPES)
    points = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = DashboardProfileManager()

    history = HistoricalRecords()

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to.",
        related_name="dashboardprofile_groups",
        related_query_name="dashboardprofile",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="dashboardprofile_user_permissions",
        related_query_name="dashboardprofile",
    )

    @property
    def calc_IMC(self):
        if self.weigth is None or self.heigth is None:
            return None

        return round(self.weigth / pow(self.heigth, 2), 2)

    def class_IMC(self):
        imc = self.calc_IMC
        if imc is None:
            return "erro, não classificado", None

        tabela_imc = {
            "Magreza": {"min": 0, "max": 18.5, "grau_obesidade": "0"},
            "Normal": {"min": 18.5, "max": 24.9, "grau_obesidade": "0"},
            "Sobrepeso": {"min": 25, "max": 29.9, "grau_obesidade": "I"},
            "Obesidade": {"min": 30, "max": 39.9, "grau_obesidade": "II"},
            "Obesidade Grave": {
                "min": 40,
                "max": float("inf"),  # infinito (não há limite superior)
                "grau_obesidade": "III",
            },
        }

        for classification, data in tabela_imc.items():
            if data.get("min") <= imc and imc <= data.get("max"):
                return classification, data.get("grau_obesidade")
        return "erro, não classificado", None

    @property
    def imc_classification(self):
        classification, _ = self.class_IMC()
        return classification

    @property
    def imc_degree(self):
        _, degree = self.class_IMC()
        return degree

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfis"
