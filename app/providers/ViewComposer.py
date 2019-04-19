""" A ViewComposer Service Provider """

from masonite.provider import ServiceProvider
from masonite.request import Request
from masonite.view import View


class ViewComposer(ServiceProvider):
    """Provides Services To The Service Container
    """

    wsgi = False
    
    def register(self):
        """Register objects into the Service Container
        """
        
        pass

    def boot(self, view:View, request:Request):
        """Boots services required by the container
        """
        view.share({'request':request})