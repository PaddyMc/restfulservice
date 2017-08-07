from django.db import models

class Player(models.Model):
	player_id = models.AutoField(primary_key=True)
	player_name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	date_of_registration = models.DateField()


class Items(models.Model):
	item_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=300)