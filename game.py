#!/usr/bin/python

import step
import json

class Game():
	
	def __init__(self, contentFile):
		self.steps = []
		self.answers = []
		text = open(contentFile).read()
		for stepText in json.loads(text):
			self.steps.append(step.Step(stepText))
		
	def start(self):
		finished = False
		while finished == False:
			for step in self.steps:
				self._clear()
				print step
				userInput = self._readUserInput(step.getPrompt(), step.getChoiceKeys())
				if step.getReportState() == True:
					self.answers.append({"title": step.data["title"], "input": step.getChoiceValue(userInput)})
			self._clear()
			for answer in self.answers:
				print "%s:\n%s\n\n" % (answer["title"], answer["input"])
			print "Bist du zufrieden mit deinem Bericht und moechtest ihn beim Vorsitzenden der Untersuchungskommission vorlegen?\n"
			print "a Ja, ich moechte meinen Bericht abschliessen."
			print "b Nein, ich moechte meinen Bericht bearbeiten."
			if self._readUserInput("Wie entscheidest du dich? ", ["a", "b"]) == "a":
				finished = True
		self._clear()
		print "\n\nDer Vorsitzende bedankt sich und teilt dir mit, dass dein Bericht von der Bundesregierung als Verschlusssache deklariert wurde. Damit ist er bis 2072 unter Verschluss. Er raet dir, diesen Bericht so schnell wie moeglich zu vergessen und nie wieder darueber zu sprechen.\n\n"				
			
	def _clear(self):
		print "\033c"
		
	def _readUserInput(self, prompt, choiceKeys):
		userInput = raw_input(prompt).lower()
		while not (userInput in choiceKeys):
			userInput = raw_input(prompt).lower()
		return userInput
		
	
if __name__ == "__main__":
	g = Game("text.txt")
	g.start()