import datetime

from django.db import models
# Create your models h ere.

class user(models.Model):
    user_id = models.CharField(primary_key=True,max_length=20)
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)

    login = "online"
    logout = "offline"
    userstate = (
        (login, "online"),
        (logout, "offline")
    )
    user_state = models.CharField(choices=userstate, max_length=20, default="offline")
    registDate = models.DateTimeField("date registed")
    #userpersonal = models.ForeignKey(userpersonal)

    #def __str__(self):
        #return self.user_name
    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            else:
                d[attr] = getattr(self, attr)

        import json
        return json.dumps(d)


#class userInformation(models.Model):
    #user_Identity_id = models.CharField(max_length=18, primary_key=True)
    #user_Identity_name = models.CharField(max_length=20)
    #user_id = models.ForeignKey(user, on_delete=models.CASCADE)

    #def __str__(self):
        #return self.user_Identity_name


class userfiles(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=200)
    user_file = models.FileField(upload_to = './upload/')

#class userpersonal(models.Model):

