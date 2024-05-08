from twisted.internet import protocol

class MyServerProtocol(protocol.Protocol):
    def __init__(self):
        self.users = {}
        
    def connectionMade(self):
        print("Client connected")

    def dataReceived(self, data):
        print(f"Received data: {data.decode()}")

    def connectionLost(self, reason):
        print("Client disconnected")
