from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from itop import login
def index(request):
    org_id=2
   

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        loger= login.Dashboard()
        saeed=loger.Login(username,password)
        print(saeed)

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

    if org_id==1: org_id="Login Failed"
    elif org_id==0: org_id="Login Success"
    else: org_id=""
    return render(request,'index.html',{"org_id":org_id})
