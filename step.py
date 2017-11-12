#!/usr/bin/python

class Step():
	
	def __init__(self, data):
		self.data = data
		self.txt = self.buildTxt(self.data)
		self.keys = self.buildChoiceKeys(self.data)
		self.prompts = self.buildPrompt(self.data)
		self.reportState = self.buildReportStates(self.data)
		
	def buildTxt(self, data):
		txt = ""
		txt += "%s\n" % str(data["title"])
		txt += "\n"
		txt += "%s\n" % str(data["text"])
		txt += "\n"
		for choice in data["choices"]:
			txt += "%s: %s\n\n" % (str(choice["choiceKey"]), str(choice["choiceValue"]))
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
			
	def buildPrompt(self, data):
		prompts = ""
		prompts += str(data["prompt"])
		prompts += " "
		return prompts
		
	def getPrompt(self):
		return self.prompts
		
	def buildReportStates(self, data):
		if (data["report"] == u"yes"):
			return True
		else:
			return False
		
	def getReportState(self):
		return self.reportState
		
	def __str__(self):
		return self.txt
		
	
		
		