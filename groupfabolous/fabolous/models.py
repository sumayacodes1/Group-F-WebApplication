from django.db import models

from django.db import models


class Department(models.Model):
    number = models.CharField(max_length=20, primary_key=True)
    type = models.CharField(max_length=200)
    summary = models.CharField(max_length=50, default="No summary provided")

def __str__(self):
    return f"(self.number) - {self.type}"

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


class Department_Leaders(models.Model):
    department = models.CharField(max_length=50, primary_key=True)
    departmentViewTeams = models.CharField(max_length=50)
    departmentViewCards = models.CharField(max_length=50)
    departmentSummaries = models.CharField(max_length=40)
    Senior_Lead = models.ForeignKey(Senior_Lead, on_delete=models.CASCADE)

class Senior_Lead(models.Model):
    seniorLeadId = models.CharField(max_length=40, primary_key=True)
    position = models.CharField(max_length=4)
    TeamManagement = models.CharField(max_length=60)
    healthcheckStatus = models.CharField(max_length=40)
    position = models.CharField(max_length=4)
    TeamManagement = models.CharField(max_length=60)
    healthcheckStatus = models.CharField(max_length=40)

