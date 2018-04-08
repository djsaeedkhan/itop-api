from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login

from itop import ItopApi
def index(request):
    status=""
    if request.method == 'POST':
        username=(request.POST.get('username'))
        password=(request.POST.get('password'))
        loger= ItopApi.Dashboard()
        status=loger.Login(username,password)
        if status== True:
            request.session['username'] = username
            request.session['password'] = password
        else:
            status="Failed Login"


    #request.session['name'] = 'Ludwik'
    #print (request.session['name'])

        #itop = itopy.Api()
        #org_id=itop.connect("https://demo.combodo.com/simple/webservices/rest.php", "1.3", username, password)
        #login()
        #tem=login 
        #if(tem==true)
        #print(org_id)

        #org_id2 = itop.get('UserLocal', 'SELECT UserLocal WHERE login="'+username+'"')
        ##print(org_id2)
        ##if org_id!=0: org_id=1


    #org_id = itop.get('Organization', 'SELECT Organization WHERE id = "192"')
    #org_id = itop.get('Person', "SELECT Person WHERE email LIKE '%.com'","email")
    #org_id = itop.get('Person', 'SELECT Person WHERE id="76"')
    
    #print(org_id)
    #return HttpResponse(html)

    return render(request,'index.html',{"status":status})
