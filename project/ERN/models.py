from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#to not confuse Django's users model
class App_User(AbstractUser):
    icon = models.CharField(max_length=100)#save url
    def __str__(self):
        return self.username
    
class Normal_Relic(models.Model):
    name = models.CharField(max_length=20)
    buff_1 = models.CharField(max_length=20, blank=True, null=True)
    buff_2 = models.CharField(max_length=20, blank=True, null=True)
    buff_3 = models.CharField(max_length=20, blank=True, null=True)
    icon_relic = models.CharField(max_length=100)#save url
    relic_type = models.CharField(max_length=20)
    relic_color = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.name} ({self.get_relic_type_display()})"
    
class Cursed_Relic(models.Model):
    name = models.CharField(max_length=20)
    buff_1 = models.CharField(max_length=20, blank=True, null=True)
    buff_2 = models.CharField(max_length=20, blank=True, null=True)
    buff_3 = models.CharField(max_length=20, blank=True, null=True)
    debuff_1 = models.CharField(max_length=20, blank=True, null=True)
    debuff_2 = models.CharField(max_length=20, blank=True, null=True)
    debuff_3 = models.CharField(max_length=20, blank=True, null=True)
    cursed_relic_type = models.CharField(max_length=20)
    cursed_icon_relic = models.CharField(max_length=100)#save url
    cursed_relic_color = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}: {self.buff_1} {self.buff_2} {self.buff_3}"

class Character(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    icon = models.CharField(max_length=500)#save url


class Build(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    relic_1 = models.ForeignKey(Normal_Relic, on_delete=models.SET_NULL, null=True, related_name='builds_relic1')
    relic_2 = models.ForeignKey(Normal_Relic, on_delete=models.SET_NULL, null=True, related_name='builds_relic2')
    relic_3 = models.ForeignKey(Normal_Relic, on_delete=models.SET_NULL, null=True, related_name='builds_relic3')
    cursed_relic_1 = models.ForeignKey(Cursed_Relic, on_delete=models.SET_NULL, null=True, blank=True, related_name='builds_cursed1')
    cursed_relic_2 = models.ForeignKey(Cursed_Relic, on_delete=models.SET_NULL, null=True, blank=True, related_name='builds_cursed2')
    cursed_relic_3 = models.ForeignKey(Cursed_Relic, on_delete=models.SET_NULL, null=True, blank=True, related_name='builds_cursed3')
    

    @property
    def likes(self):
        return self.votes.filter(vote_type = True).count()
    @property
    def dislike(self):
        return self.votes.filter(vote_type = False).count()
    
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='character_build')
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at', 'is_public']),
            models.Index(fields=['character']),
            models.Index(fields=['user', 'created_at'])
        ]
    
    def __str__(self):
        return f"{self.title} - {self.character.name}"
    
class Build_Vote(models.Model):
    LIKE = True
    DISLIKE = False
    VOTE_CHOICES = [(True, 'Like'), (False, 'Dislike')]
    
    build = models.ForeignKey(Build, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    vote_type = models.BooleanField(choices=VOTE_CHOICES)  # True=like, False=dislike
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        unique_together = ['build', 'user']  # un voto por usuario por build


