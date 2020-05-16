from django.shortcuts import render
from .models import Modify
def cheese(request):
   mod1=Modify()
   mod1.name='Jalebi'
   mod1.desc='A sweet dish serve in breakfast along with curd.'
   mod1.price='Rs 45/250g'
   return render(request,'1.html',{'mod1':mod1})
