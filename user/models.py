from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class ProfileManager(models.Manager):
    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Relationship.objects.filter(Q(sender=profile)| Q(receiver=profile))
        print(qs)
        accepted = set([])
        for rel in qs:
            if rel.status == "accepted":
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        print(accepted)
        available = [profile for profile in profiles if profile not in accepted]
        print(available)
        return available

    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete =  models.CASCADE)
    image = models.ImageField(default ="default.jpg", upload_to="./profile_pics")
    interests = models.CharField(max_length=350,verbose_name="interests", default="Who am I?")
    youtube_id = models.CharField(max_length=100,verbose_name="youtube", default="youtube")
    instagram_id = models.CharField(max_length=100,verbose_name="instagram", default="instagram")
    facebook_id = models.CharField(max_length=100,verbose_name="facebook", default="facebook")
    twitter_id = models.CharField(max_length=100,verbose_name="twitter",default="twitter")
    soundcloud_id = models.CharField(max_length=100,verbose_name="soundcloud",default="soundcloud")
    spotify_id = models.CharField(max_length=100,verbose_name="spotify",default="spotify")       
    phone = models.CharField(max_length=100,verbose_name="phone", default="phone")
    email = models.CharField(max_length=100,verbose_name="email", default="email")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")

    objects = ProfileManager()

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    def __str__(self):
        return f'{self.user.username} Profile' 

STATUS_CHOICES = (
    ("send", "send"),
    ("accepted","accepted"),
)

class RelationshipManager(models.Manager):
    def invitations_received(self, receiver):
        qs = Relationship.objects.filter(receiver = receiver, status='send')
        return qs



class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=8, choices = STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"


