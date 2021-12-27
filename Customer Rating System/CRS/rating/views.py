from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from .models import Rules
from .models import Account_info
from .models import Customer_info
from .models import Countries
import datetime
# Create your views here.
def rating(request):
   return render(request,'index.html')
 

def output(request):
   rules=list(Rules.objects.all().filter(applied=True))
   ak=request.POST['accountKey']
   temp=Account_info.objects.all().filter(account_key=ak)
   risk_status=None
   risk_reason=None
   if len(Transactions.objects.filter(acc_key=ak)) > 10:
      risk_status='H1'
      risk_reason='no of transaction is greater than 10'
   elif len(Transactions.objects.filter(acc_key=ak)) < 10:
      t=Transactions.objects.filter(acc_key=ak).filter(transaction_type='INN')
      t1=Transactions.objects.filter(acc_key=ak).filter(transaction_type='OUT')
      s=0
      for i in t:
         s+=i.transactionamount
      if s>1000 :
         risk_status='H2'
         risk_reason=' sum of incomming transacrtion is greatyer than 1000'
      s=0
      for i in t1:
         s+=i.transactionamount
      if s>800:
         risk_status='H3'
         risk_reason='sum of outgoing  transacrtion is greatyer than 800'
   elif len(Transactions.objects.filter(acc_key=ak)) > 20:
      risk_status='H4'
      risk_reason='no of transaction is > 20'
         
   if len(Transactions.objects.filter(acc_key=ak)) > 6:
      risk_status='M1'
      risk_reason='no of transaction is greater than 6'
   elif len(Transactions.objects.filter(acc_key=ak)) < 6:
      t=Transactions.objects.filter(acc_key=ak).filter(transaction_type='INN')
      t1=Transactions.objects.filter(acc_key=ak).filter(transaction_type='OUT')
      s=0
      for i in t:
         s+=i.transactionamount
      if s>600 and s<1000 :
         risk_status='M2'
         risk_reason='no of transaction is < 6 but sum of transacrtion is greatyer than 1000'
      s=0
      for i in t1:
         s+=i.transactionamount
      if s>500 and s<800:
         risk_status='M3'
         risk_reason='no of transaction is < 6 but sum of transacrtion is greatyer than 800'
   elif len(Transactions.objects.filter(acc_key=ak)) > 10 and len(Transactions.objects.filter(acc_key=ak))<20:
      risk_status='M4'
      risk_reason='no of transaction is > 10 and < 20'
      
   if len(Transactions.objects.filter(acc_key=ak)) < 10:
      risk_status='L1'
      risk_reason='no of transaction is less than 10'
   elif len(Transactions.objects.filter(acc_key=ak)) > 10:
      t=Transactions.objects.filter(acc_key=ak).filter(transaction_type='INN')
      t1=Transactions.objects.filter(acc_key=ak).filter(transaction_type='OUT')
      s=0
      for i in t:
         s+=i.transactionamount
      if s<600 :
         risk_status='L2'
         risk_reason='sum of incomming transactions is less than 600'
      s=0
      for i in t1:
         s+=i.transactionamount
      if s<500:
         risk_status='L3'
         risk_reason='sum of outgoing transactions is less than 500'
   elif len(Transactions.objects.filter(acc_key=ak)) < 10 :
      risk_status='L4'
      risk_reason='no of transactions is less than 10'
   
      
      
      
      
   a=Transactions.objects.filter(acc_key=ak)
   customers = Customer_info.objects.all();
   return render(request,'output.html',{'Customer_Name':customers[0].partykey,'Residential_Country':(customers[0].resident_country).rel_key,'Risk_Rating':risk_status,'Risk_Rating_Reason':risk_reason})