from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings
from core.models import UserInfo


    
#Define the connection relation
class ConnectionManager(models.Manager):
    
    def connection_for_user(self, user):
        connections = []
        for connection in self.filter(host_user=user).select_related(depth=1):
            connections.append({"neighbor": connection.host_user, "connection": connection})
        for connection in self.filter(end_user=user).select_related(depth=1):
            connections.append({"neighbor": connection.end_user, "connection": connection})
        return connections
    
    def are_neighbors(self, user1, user2):
        if self.filter(end_user=user1, host_user=user2).count() > 0:
            return True
        if self.filter(end_user=user2, host_user=user1).count() > 0:
            return True
        return False
    
    def remove(self, user1, user2):
        if self.filter(end_user=user1, host_user=user2):
            connection = self.filter(end_user=user1, host_user=user2)
        elif self.filter(end_user=user2, host_user=user1):
            connection = self.filter(end_user=user2, host_user=user1)
        connection.delete()
        
class Connection(models.Model):
    #A connection is a bi-directional association between two users who
    #have both agreed to the association.
    #from site: https://github.com/jtauber/django-friends/blob/master/friends/models.py
        
    host_user = models.ForeignKey(UserInfo, related_name="host_id") #was to_user
    end_user = models.ForeignKey(UserInfo, related_name="enduser_id") #was from_user
    # @@@ relationship types
    added = models.DateField(default=datetime.date.today)
    intro_message = models.CharField("Intro Message to Host from User", max_length=300, null=True,blank=True)
    pickup_time = models.CharField("Preferred Pickup Time", max_length=150, blank=True, null=True)
    testfield=models.CharField(max_length=200,blank=True, null=True)
    objects = ConnectionManager()
    
    class Meta:
        unique_together = (('host_user', 'end_user'),)
