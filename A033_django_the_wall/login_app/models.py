from django.db import models
import bcrypt, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        
        # 2 charcters min for first/last name
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters."
        
        # valid email format
        if not EMAIL_REGEX.match(postData['reg_email']):
            errors['reg_email'] = "Email format incorrect."

        # matching passwords between pw and confirm pw fields
        if not postData['reg_confirm_pw'] == postData['reg_pw']:
            errors['reg_confirm_pw'] = "Password confirmation must match password."

        # passwords at least 8 characters
        if len(postData['reg_pw']) < 8:
            errors['reg_pw'] = "Password should be at least 8 characters."

        return errors

    def login_user(self, request):
        # verify if user email exists
        user = User.objects.filter(email=request.POST['login_email'])
        if user:
            # verify password hashes match
            if bcrypt.checkpw(request.POST['login_pw'].encode(), user[0].pw.encode()):
                return user
        return False

    def register_user(self, request):
        # verify if user already exists
        user = self.filter(email=request.POST['reg_email'])
        if not user:
            first = request.POST['first_name']
            last = request.POST['last_name']
            email = request.POST['reg_email']
            pw_hashed = bcrypt.hashpw(request.POST['reg_pw'].encode(), bcrypt.gensalt()).decode()

            user = self.create(first=first, last=last, email=email, pw=pw_hashed)
            return user
        else:
            return False

class User(models.Model):
    first = models.CharField(max_length=60) 
    last = models.CharField(max_length=60)
    email = models.EmailField(max_length=255, unique=True)
    pw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"User: {self.first} {self.last} {self.email}"
