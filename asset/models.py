from django.db import models
from django.conf import settings
from django.urls import reverse
import datetime

# Create your models here.
class Asset(models.Model):
	CATEGORY=(
		('COMPUTERS','COMPUTER'),
		('FURNITURES','FURNITURE'),
		('OFFICE_EQUIPMENT','OFFICE EQUIPMENT'),
		('LINK_EQUIPMENT','LINK EQUIPMENT'),
		('SERVERS','SERVERS'),
		)	
	
	asset_description=models.TextField(max_length=100)
	tag_number=models.TextField(unique=True)
	voucher_number=models.TextField(null=True)	
	serial_number=models.TextField(default='None')
	category=models.TextField(choices=CATEGORY)
	location=models.TextField(max_length=200)
	date_in_service=models.DateField(default=datetime.date.today)
	
	class Meta:
		ordering=('id',)
	

	def __str__(self):
		return self.asset_description


	def get_absolute_url(self):
		return reverse('main:AssetDetail',kwargs={'pk':self.id})
