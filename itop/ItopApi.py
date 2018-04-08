from itop import itopy

class MyException(Exception):
    """
    Handle custom exceptions
    """
    pass

class Dashboard(object):
    
    """
    To instanciate an itopy object.
    No parameter needed.
    """
    def __init__(self):
        """
        Just init
        """
        pass
    def connect(self,username,password):
        itop = itopy.Api()
        return itop.connect("https://demo.combodo.com/simple/webservices/rest.php", "1.3", username, password)

    def Login(self,username,password):
        status=2
        org_id=self.connect(username,password)
        if org_id==0: 
            status=True
        else:
            status=False
        return status

    def UserLocal(self,request):
        username=request.session['username']
        password=request.session['password']

        itop = itopy.Api()
        itop.connect("https://demo.combodo.com/simple/webservices/rest.php", "1.3", username, password)

        org_id2 = itop.get('UserLocal', 'SELECT UserLocal WHERE login="'+username+'"')
        return org_id2