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
		for step in self.steps:
			self._clear()
			print step
			userInput = self.readUserInput(step)
			self.answers.append(step.getChoiceValue(userInput))
		self._clear()
		for answer in self.answers:
			print answer
			
	def _clear(self):
		print "\033c"
		
	def readUserInput(self, step):
		userInput = raw_input("Was willst du tun? ").lower()
		while not (userInput in step.getChoiceKeys()):
			userInput = raw_input("Was willst du tun? ").lower()
		return userInput
		
	
if __name__ == "__main__":
	g = Game("text.txt")
	g.start()