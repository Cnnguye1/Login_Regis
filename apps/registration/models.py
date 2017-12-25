from __future__ import unicode_literals
import re
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class RegisManager(models.Manager):
	def validate(self, post_data):
		errors = {}
		for field, value in post_data.iteritems():
			if len(value) < 1:
				errors[field] = '{} field is required'.format(field.replace('_', ' '))
			if field == 'first_name' or field == 'last_name':
				if not field in errors and len(value) < 2:
					errors[field] = '{} field must be at least 2 characters'.format(field.replace('_', ' '))
				if field == 'password':
					if not field in errors and len(value)<8:
						errors[field] = '{} field must be at least 8 characters'.format(field)
		if not 'email' in errors and not EMAIL_REGEX.match(post_data['email']):
			errors['email'] = 'invalid email'
		if post_data['password'] != post_data['comfirm_pw']:
			errors['comfirm_pw'] = 'invalid comfirm password'
		return errors

class Registration(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = RegisManager()
	def __str__(self):
		return self.email
		