from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#to not confuse Django's users model
class App_User(AbstractUser):
    icon = models.ImageField(upload_to='users_icon/', blank=True, null=True)
    def __str__(self):
        return self.username
    
class Normal_Relic(models.Model):
    RELIC_TYPES = [
        ('RED', 'Red'),
        ('BLUE', 'Blue'),
        ('GREEN', 'Green'),
        ('YELLOW', 'Yellow'),
        ('SMALL_YELLOW', 'Small Yellow'),
        ('SMALL_RED', 'Small Red'),
        ('SMALL_BLUE', 'Small Blue'),
        ('SMALL_GREEN', 'Small Green'),
    ]
    
    name = models.CharField(max_length=100)
    buff_1 = models.CharField(max_length=20, blank=True, null=True)
    buff_2 = models.CharField(max_length=20, blank=True, null=True)
    buff_3 = models.CharField(max_length=20, blank=True, null=True)
    icon_relic = models.ImageField(upload_to='relics/normal/', blank=True, null=True)
    relic_type = models.CharField(max_length=20, choices=RELIC_TYPES)
    
    def __str__(self):
        return f"{self.name} ({self.get_relic_type_display()})"
    
class Cursed_Relic(models.Model):
    CURSED_RELIC_TYPES = [
        ('CURSED_RED', 'Cursed Red'),
        ('CURSED_GREEN', 'Cursed Green'),
        ('CURSED_YELLOW', 'Cursed Yellow'),
        ('CURSED_BLUE', 'Cursed Blue'),
    ]
    name = models.CharField(max_length=20)
    buff_1 = models.CharField(max_length=20, blank=True, null=True)
    buff_2 = models.CharField(max_length=20, blank=True, null=True)
    buff_3 = models.CharField(max_length=20, blank=True, null=True)
    debuff_1 = models.CharField(max_length=20, blank=True, null=True)
    debuff_2 = models.CharField(max_length=20, blank=True, null=True)
    debuff_3 = models.CharField(max_length=20, blank=True, null=True)
    cursed_relic_type = models.CharField(max_length=20,choices=CURSED_RELIC_TYPES)
    cursed_icon_relic = models.ImageField(upload_to='relics/cursed/', blank=True, null=True)
    def __str__(self):
        return f"{self.name} ({self.get_cursed_relic_type_display()})"

class Character(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    icon = models.ImageField(upload_to='characters/', blank=True,null=True)


class Build_Tag(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    def __str__(self):
        return self.name

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
    liked = models.IntegerField(default=0)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='character_build')
    author_name = models.CharField(max_length=100, blank=True)
    is_public = models.BooleanField(default=True)
    tags = models.ManyToManyField(Build_Tag, blank=True, related_name='build_tag')
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-liked', '-created_at']  #sorted by newest and liked ones
        indexes = [
            models.Index(fields=['created_at', 'is_public']),
            models.Index(fields=['character', 'liked']),
            models.Index(fields=['user','created_at'])
        ]
    
    def __str__(self):
        return f"{self.title} - {self.character.name}"
    
class Build_Vote(models.Model):
    build = models.ForeignKey(Build, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        unique_together = ['build', 'user']


