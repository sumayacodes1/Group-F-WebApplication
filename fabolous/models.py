from django.db import models



class Department(models.Model):
    number = models.CharField(max_length=20, primary_key=True)
    type = models.CharField(max_length=200)
    summary = models.CharField(max_length=50, default="No summary provided")
    
class User(models.Model):
    userName = models.CharField(max_length=40)
    fullName = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    password=models.CharField(max_length=100, null=True, blank=True)
    team_leaderFlag=models.BooleanField(default=False)
    team_leaderId= models.CharField(max_length=20, blank=True, null=True)
    roles_flag= models.BooleanField(default=True)
    roles=models.CharField(max_length=100, null=True, blank=False)
    engineer_flag=models.BooleanField(default=True)
    engineer_id=models.CharField(max_length=20, null=True,blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)





class Team(models.Model):
    team_id = models.CharField(max_length=30)
    team_Summary = models.CharField(max_length=200, null=True, blank=True, )
    create_date = models.DateTimeField(auto_now=True)
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Health_Check_Card(models.Model):
    STATUS_CHOICES = [
    ('green', 'Green'),
    ('amber', 'Amber'),
    ('red', 'Red'),
    ]
    card_id= models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=True )
    comments = models.TextField(blank=True)
    team_id = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True )
    




