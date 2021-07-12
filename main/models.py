from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from datetime import datetime


# class Members (models.Model):
#     # d_id = models.AutoField(primary_key=True)
#     first_name = models.CharField (max_length=100)
#     last_name = models.CharField (max_length=100)
#     email = models.EmailField ()
      
# class Meta:
#     db_table = "members"


class List (models.Model):
    first_name = models.CharField (max_length=100)
    last_name = models.CharField (max_length=100)
    email = models.EmailField ()
    gender = models.BooleanField()

class Meta:
    db_table = "members"



class Loaning (models.Model):
    borrower = models.CharField (max_length=100)
    amount = models.IntegerField()
    lender = models.CharField (max_length = 100)
    return_date = models.DateField()
    guarantors = models.CharField (max_length = 100)
    
class Meta:
    db_table = "loans"



class Saving (models.Model):
    members = models.CharField (max_length=100)
    amount = models.IntegerField()
    date = models.DateField()

class Meta:
    db_table = "saved"










# class Members(models.Model):
#     id = models.AutoField(primary_key=True)
#     admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
#     gender = models.CharField(max_length=50)
#     profile_pic = models.FileField()
#     address = models.TextField()
#     sacco_id = models.ForeignKey(Saccos, on_delete=models.DO_NOTHING, default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()

# class loans (models.Model):
#     d_id = models.ForeignKey(Members, default = 1, verbose_name = "Members", on_delete = models.SET_DEFAULT)
#     amount = models.IntegerField (max_length)
#     description = models.CharField(max_length=100)

#     class Meta:
#         verbose_name_plural = "Loans"
#         db_table = "loans"

#     def __str__(self):
#         return self.loans


# class savings (models.Model):
#     d_id = models.ForeignKey(Members, default = 1, verbose_name = "Members", on_delete = models.SET_DEFAULT)
#     amount = models.IntegerField ()
#     description = models.CharField(max_length=100)

#     class Meta:
#         verbose_name_plural = "Savings"
#         db_table = "savings"

#     def __str__(self):
#         return self.savings



# # from django.forms import ModelForm, Textarea
# # from django.forms.fields import EmailField

# # Overriding the Default Django Auth User and adding One More Field (user_type)
# class CustomUser(AbstractUser):
#     user_type_data = ((1, "SuperAdmin"), (2, "SaccoAdmin"), (3, "Member"))
#     user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

# class SuperAdmin(models.Model):
#     id = models.AutoField(primary_key=True)
#     admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()

# class SaccoAdmin(models.Model):
#     id = models.AutoField(primary_key=True)
#     admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
#     address = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()

# class Saccos(models.Model):
#     id = models.AutoField(primary_key=True)
#     sacco_name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()

#     def __str__(self):
#         return self.sacco_name





