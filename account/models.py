from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from districts.models import District


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, phone, name, password=None):
        if not email:
            raise ValueError('Users must have a valid email address')
        if not phone:
            raise ValueError('Users must have a valid phone number')
        if not name:
            raise ValueError('Users must have a name')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            phone=phone,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_agency = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, verbose_name="Email", unique=True)
    phone = models.IntegerField(verbose_name="Phone Number", unique=True)
    name = models.CharField(max_length=50, verbose_name="Full Name", unique=False)
    date_joined = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_agency = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_district = models.ForeignKey(District, on_delete=models.PROTECT, blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'name',]

    objects = MyUserManager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_active
