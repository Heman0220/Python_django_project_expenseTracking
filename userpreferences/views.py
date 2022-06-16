from locale import currency
from pdb import Pdb
from django.shortcuts import render
import os
import json
from django.conf import settings
from numpy import save
from .models import Userpreferences,User
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def preferences(request):

    if request.method=='POST':
       exists=Userpreferences.objects.filter(user=request.user).exists()
       currency = request.POST.get('currency')
       if exists:   
          user_pref=Userpreferences.objects.get(user=request.user)
          print("currency",currency,exists)
          user_pref.save()
          print('user currency',user_pref.currency)
          return render(request,'preferences/index.html')
       else:
            user_pref=Userpreferences.objects.create(user=request.user,currency=currency)
            user_pref.save()
            print('user currency',user_pref.currency)
            return render(request,'preferences/index.html',{'user_pref':user_pref})     
    else:        
      currency_data=[]
      file_path=os.path.join(settings.BASE_DIR,'currencies.json')
      with open(file_path,'r') as json_file:
          data=json.load(json_file)
      # import pdb
      # pdb.set_trace() 
      for i,j in data.items():
          currency_data.append({'name':i,'value':j})
      context={
        'currency_data':currency_data
      }    

      return render(request,'preferences/index.html',context)