from django.db import models
from django.urls import reverse

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    title=models.CharField(max_length=256)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse('my_app:post_list')


    def publish(self):
        print("hey")
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post=models.ForeignKey('Post',related_name="Comment",on_delete=models.CASCADE)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.author)


    def get_absolute_url(self):
        return reverse('my_app:post_list',kwargs={'pk':self.post.pk})


CHOICES = (
    ('mentor','MENTOR'),
    ('student', 'STUDENT'),
)

class User_info(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    profilepic=models.ImageField(blank=True,upload_to='profilePic')
    type_of_user=models.CharField(max_length=250,choices=CHOICES,default='student')
    facebook = models.CharField(max_length=50, default='facebook login')
    
    def __str__(self):
        return self.username.username

class Pairing(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    mentor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    money = models.IntegerField(default = 0)
    Ack1 = models.BooleanField(default = True)
    Ack2 = models.BooleanField(default = False)
    Ack3 = models.BooleanField(default = False)
    Ack4 = models.BooleanField(default = False)
    
    def __str__(self):
        return str(self.mentor)