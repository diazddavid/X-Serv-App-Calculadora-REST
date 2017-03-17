#!/usr/bin/python3

"EVERY CLASSES IMPLEMENT APP FROM WEBAPP.PY"

import single_sesion

class op():

    op1 = 0
    op2 = 0

class add(single_sesion.app):

    "Sum use default parse"

    def process(self, parsedRequest, method):
        if method == "GET":
            return("200 OK", "<html><body><h1>La suma es :</h1>" +
                            "<p>" + str(op.op1) + " + " + str(op.op2) +
                            " = " + str(op.op1 + op.op2) + "</p>" +
                            "</body></html>")
        else:
            return("400 Bad request", "<html><body><h1>METODO ERRONEO, USE GET</h1></body></html>")

class sub(single_sesion.app):

    "Sum use default parse"

    def process(self, parsedRequest, method):
        if method == "GET":
            return("200 OK", "<html><body><h1>La resta es :</h1>" +
                            "<p>" + str(op.op1) + " - " + str(op.op2) +
                            " = " + str(op.op1 - op.op2) + "</p>" +
                            "</body></html>")
        else:
            return("400 Bad request", "<html><body><h1>METODO ERRONEO, USE GET</h1></body></html>")

class mul(single_sesion.app):

    "Sum use default parse"

    def process(self, parsedRequest, method):
        if method == "GET":
            return("200 OK", "<html><body><h1>La multiplicacion es :</h1>" +
                            "<p>" + str(op.op1) + " * " + str(op.op2) +
                            " = " + str(op.op1 * op.op2) + "</p>" +
                            "</body></html>")
        else:
            return("400 Bad request", "<html><body><h1>METODO ERRONEO, USE GET</h1></body></html>")

class div(single_sesion.app):

    "Sum use default parse"

    def process(self, parsedRequest, method):
        if method == "GET":
            return("200 OK", "<html><body><h1>La division es:</h1>" +
                            "<p>" + str(op.op1) + " / " + str(op.op2) +
                            " = " + str(op.op1 / op.op2) + "</p>" +
                            "</body></html>")
        else:
            return("400 Bad request", "<html><body><h1>METODO ERRONEO, USE GET</h1></body></html>")

class init(single_sesion.app):

    def parse(self, request, rest):
        method = request.split(' ', 2)[0]
        body = request.splitlines()[10]
        if '&' in body:
            return([body.split("&")[0], body.split("&")[1]], method)
        else:
            return([0, 0], method)

    def process(self, parsedRequest, method):
        if method == "PUT":
            op.op1 = int(parsedRequest[0])
            op.op2 = int(parsedRequest[1])
            return("200 OK", "<html><body><h1>Ha añadido:</h1>" +
                            str(op.op1) + " y " +
                            str(op.op2) + "</body></html>")
        else:
            return("400 Bad request", "<html><body><h1>METODO ERRONEO, USE GET</h1></body></html>")
