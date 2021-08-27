from django.db import models
import re
import bcrypt


class User_Manager(models.Manager):
    def user_validator(self, post_data):
        errors = {}
        return errors


class Message_Manager(models.Manager):
    def message_validator(self, post_data):
        errors = {}
        return errors
    
class Comment_Manager(models.Manager):
    def comment_validator(self, post_data):
        errors = {}
        return errors
    


class User(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_level = models.DecimalField(max_digits=1, decimal_places=0)
    objects = User_Manager()
    
class Message(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Message_Manager()
    
class Comment(models.Model):
    comment = models.TextField()
    commented_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    commented_on = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Comment_Manager()
    
    
