from twisted.internet import protocol
from .protocol import MyServerProtocol

class MyServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return MyServerProtocol()
