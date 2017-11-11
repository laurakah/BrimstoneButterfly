#!/usr/bin/python

class Step():
	
	def __init__(self, data):
		self.data = data
		self.txt = self.buildTxt(self.data)
		self.keys = self.buildChoiceKeys(self.data)
		
	def buildTxt(self, data):
		txt = ""
		txt += "%s\n" % data["title"]
		txt += "\n"
		txt += "%s\n" % data["text"]
		txt += "\n"
		for choice in data["choices"]:
			txt += "%s: %s\n" % (choice["choiceKey"], choice["choiceValue"])
		return txt
		
	def buildChoiceKeys(self, data):
		keys = []
		for choice in self.data["choices"]:
			keys.append(choice["choiceKey"])
		return keys
		
	def getChoiceKeys(self):
		return self.keys
		
	def getChoiceValue(self, key):
		for choice in self.data["choices"]:
			if key != choice["choiceKey"]:
				continue
			return choice["choiceValue"]
		
	def __str__(self):
		return self.txt
		
	
		
		