from django.db import models

# Create your models here.
# validators to validate the fields in model. ensures legit combination of characters

from django.core.validators import RegexValidator

from django.contrib.auth.models import (
		BaseUserManager, AbstractBaseUser
	)

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'

#specify all the methods that can happen on that actual model

class MyUserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
	        #if there is no email there will be error

		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
		            #passing the field

					username = username,
					email = self.normalize_email(email)
				)
				        #set password for user

		user.set_password(password)
		user.save(using=self._db) #basically specifying the database. save in the database which is specified in settings
		return user
		# user.password = password # bad - do not do this

	def create_superuser(self, username, email, password=None):
	        # passing an create_user method. and inside the method passing parameters

		user = self.create_user(
				username, email, password=password
			)
		user.is_admin = True #when creating superuser. Its gonna call create_user method coming from models below
		user.is_staff = True
		user.save(using=self._db)
		return user


#Explicitly, this is our own user

class MyUser(AbstractBaseUser):
	username = models.CharField(
					max_length=255,
					validators = [
						RegexValidator(regex = USERNAME_REGEX,
										message='Username must be alphanumeric or contain numbers',
										code='invalid_username'
							)],
					unique=True
				)
	email = models.EmailField(
			max_length=255,
			unique=True,
			verbose_name='email address'
		)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

    #bojects of this model refers to object manager. Object goes to user manager
	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email'] #fields that can be specified in models

	def __str__(self):
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email


	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True