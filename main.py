from twisted.internet import reactor
from server.factory import MyServerFactory

def main():
    port = 12345
    factory = MyServerFactory()
    reactor.listenTCP(port, factory)
    print(f"Server started and listening on port {port}")
    reactor.run()

if __name__ == "__main__":
    main()
