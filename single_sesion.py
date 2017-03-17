#!/usr/bin/python3

"""
webAppMulti class
Root for hierarchy of classes implementing web applications
Each class can dispatch to serveral web applications, depending
on the prefix of the resource name
Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles (2009-15)
jgb @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
October 2009, February 2015
"""

import socket
import calc

class app:
    """Application to which webApp dispatches. Does the real work
    Usually real applications inherit from this class, and redefine
    parse and process methods"""

    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information.
        request: HTTP request received from the client
        rest:    rest of the resource name after stripping the prefix
        """

        return (None, request.split(' ', 2)[0])

    def process(self, parsedRequest, method):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>" +
                          "Bienvenido, puede /add, /sub, /div, /mul. Pero primero /new/numeros, formato: NUM&NUM" +
                          "</h1></body></html>")

class webApp:
    """Root of a hierarchy of classes implementing web applications
    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """

    def select(self, request):
        """Selects the application (in the app hierarchy) to run.
        Having into account the prefix of the resource obtained
        in the request, return the class in the app hierarchy to be
        invoked. If prefix is not found, return app class
        """

        resource = request.split(' ', 2)[1]
        for prefix in self.apps.keys():
            if resource.startswith(prefix):
                print("Running app for prefix: " + prefix + \
                    ", rest of resource: " + resource[len(prefix):] + ".")
                return (self.apps[prefix], resource[len(prefix):])
        print("Running default app")
        return(self.myApp, request)

    def __init__(self, hostname, port, apps):
        """Initialize the web application."""

        self.apps = apps
        self.myApp = app()
        op1 = 0
        op2 = 0

        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)

        while True:
            print('Waiting for connections')
            (recvSocket, address) = mySocket.accept()
            print('HTTP request received (going to parse and process):')
            request = recvSocket.recv(2048).decode('utf-8')
            print(request)
            (theApp, rest) = self.select(request)
            (parsedRequest, method) = theApp.parse(request, rest)
            (returnCode, htmlAnswer) = theApp.process(parsedRequest, method)
            print('Answering back...')
            recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n", 'utf-8'))
            recvSocket.close()

if __name__ == "__main__":
    add = calc.add()
    sub = calc.sub()
    mul = calc.mul()
    div = calc.div()
    init = calc.init()
    testWebApp = webApp("localhost", 1234, {'/add': add,
                                            '/new': init,
                                            '/sub': sub,
                                            '/mul': mul,
                                            '/div': div})
