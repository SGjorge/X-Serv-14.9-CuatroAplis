#!/usr/bin/python

class hola():

    def parse(self, request, rest):
        return "OK"

    def process(self, parsedRequest):
        return ("200 OK", "<html><body><b>Hola Mundo!</h1></body></html>")

class adios():
	def parse(self, request, rest):
		return "OK"

	def process(self, parsedRequest):
		return ("200 OK", "<html><body><b>Adios Mundo Cruel!</h1></body></html>")
