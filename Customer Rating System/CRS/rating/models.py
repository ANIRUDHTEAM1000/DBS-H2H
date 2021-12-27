from django.db import models


# Create your models here.
class Countries(models.Model):
    id = models.CharField(max_length=100)
    rel_key = models.CharField(max_length=100, primary_key=True)

class Customer_info(models.Model):
    partykey = models.CharField(max_length=100, primary_key=True)
    resident_country = models.ForeignKey(Countries, on_delete = models.CASCADE)
    party_open_date = models.DateField()

class Account_info(models.Model):
    account_key= models.CharField(max_length=100, primary_key=True)
    primary_partkey = models.ForeignKey(Customer_info, on_delete = models.CASCADE)
    account_open_date= models.DateField()
    
class Rules(models.Model):
    rule_name = models.CharField(max_length=20, primary_key=True)
    applied = models.BooleanField()

class Transactions(models.Model):
    transactionkey = models.CharField(max_length=100,primary_key=True)
    acc_key= models.ForeignKey(Account_info, on_delete = models.CASCADE)
    transactionamount = models.IntegerField()
    transaction_type=models.CharField(max_length=100)
    transaction_origin=models.ForeignKey(Countries, on_delete = models.CASCADE)
    transactiondate=models.DateField()


    



