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

    def Login(self,username,password):
        status=2
        itop = itopy.Api()
        org_id=itop.connect("https://demo.combodo.com/simple/webservices/rest.php", "1.3", username, password)

        if org_id==0: 
            status=True
        else:
            status=False

        return status