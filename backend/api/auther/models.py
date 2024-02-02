from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _ 
from django.utils import timezone
from .managers import CustomeUserManager




class BaseModel(models.Model):
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
  
   class Meta: 
        abstract = True



class CustomeUser(AbstractUser):

    class Types(models.TextChoices):
        AUTHOR = "AUTHOR", "AUTHOR"
        EDITER = "EDITER", "EDITER"
        ADMIN = "ADMIN", "ADMIN"
        
    username = None
    type = models.CharField(max_length=20, choices=Types.choices, default=Types.ADMIN)
    email = models.EmailField(_('email_address'),unique=True)
    first_name = models.CharField(_('first name'),max_length=100,blank=True)
    last_name = models.CharField(_('last name'),max_length=200,blank=True)
    mobile_number = models.CharField(_('mobile_no'),max_length=20,null=True,blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_superuser = models.BooleanField(_('superuser status'), default=False,
                                       help_text=_('Designates that this user has all permissions without explicitly assigning them.'))
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomeUserManager()

    def __str__(self):
        return self.email

