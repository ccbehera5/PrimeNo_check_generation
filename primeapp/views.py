from django.shortcuts import render
from django.http import HttpResponse
from primeapp.models import Savedata
import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')

def check(request):
    data=''
    n=''
    try:
        if request.method=="POST":
            n=eval(request.POST.get('num'))
            if n>1:
                for i in range(2,n):
                    if (n%i) == 0:
                        data='IS NOT A PRIME NUMBER'
                        break
                else:
                    data='IS A PRIME NUMBER'
            else:
                data='IS NOT VALID NUMBER'
    except:
        data='IS A INVALID INPUTE'
    return render(request,'checkprime.html',{'data':data,'n':n})
    



def generator(request):
    data1=[]
    data2=''
    n=0
    m=0
    try:
        if request.method=='POST':
            n=eval(request.POST.get('start'))
            m=eval(request.POST.get('stop'))
            if n>m:
                data2='invalid range'
            elif (m-n==1):
                data2='In between this no , No number is available'
            elif (n==m):
                data2='If start no is equal to stop no, Then prime no generation is no possible'

            else:
                for num in range(n,m+1):
                    if num>1:
                        for i in range(2,num):
                            if (num%i) == 0:
                                break
                        else:
                            data1.append(num)
                    # else:
                    #     data1='enter valid numbers'        
        
    except:
        data2='IS A INVALID INPUTE'
    current_time=datetime.datetime.now()
    database=Savedata(startno=n,stopno=m,outdata1=data1,outdata2=data2,time=current_time)
    database.save()
    return render(request, 'primegenerator.html',{'data1':data1,'n':n,'m':m,'data2':data2})

