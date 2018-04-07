import StringIO

from soaplib.wsgi import AppBase
from soaplib.service import rpc, Definition, ValidatingDefinition
from soaplib.serializers import primitive as soap_types
from django.http import HttpResponse


class DumbStringIO(StringIO.StringIO):
    def read(self, n):
        return self.getvalue()


class DjangoSoapService(ValidatingDefinition):
    # replace with your namespace URL
    __tns__ = 'http://localhost'

    @rpc(soap_types.String, _returns=soap_types.String)
    def hello_world(self, hello_string):
        """
        Accepts primitive string and returns the same primitive.
        """
        return hello_string