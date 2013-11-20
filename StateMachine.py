class StateMachine:
	def __init__(self):
		self.initialState = []
		self.finalStates = []
		self.states = []
		self.alphabet = []
		self.transitions = []

	def setInitialState(self, initialState):
		self.initialState = initialState
		
	def addFinalStates(self, finalStates):
		self.__addListTo(finalStates,"finalStates")
		
	def addStates(self, states):
		self.__addListTo(states,"states")
		
	def addAlphabet(self, alphabet):
		self.__addListTo(alphabet,"alphabet")

	def addTransitions(self, transitions):
		self.__addListTo(transitions,"transitions")
		
	def __addListTo(self, list, nameOfList):
		if nameOfList == "finalStates":
			for temp in list:
				(self.finalStates).append(temp)
		elif nameOfList == "states":
			for temp in list:
				(self.states).append(temp)
		elif nameOfList == "alphabet":
			for temp in list:
				(self.alphabet).append(temp)
		else :
			for temp in list:
				(self.transitions).append(temp)

	def getInitialState(self):
		return self.initialState[0]

	def stateMachineStart(self, inputString):
		if (self.validateValues()):
			currentState = self.getInitialState()
			finalTransitionState = self.startTransition(inputString,currentState) #  should give final transtition state 
			if(self.isFinalState(finalTransitionState)):
				print "Final State Reached ... Transition stopped at "+finalTransitionState
			else : 
				print "Invalid String Transition stopped at "+str(finalTransitionState)
		else :
			print "object values are not initialised properly ....."


	def validateValues(self):
		if (len(self.initialState) == 0 or len(self.alphabet) == 0 or len(self.transitions) == 0):
			return False
		else :
			return True

 
	def startTransition(self, inputString, currentState):
		transitionFlow = []
		transitionFlow.append(self.getInitialState())
		for c in inputString :
			nextState = self.getNextTransition(currentState,c)
			if nextState == None :
				return transitionFlow[-1]
			currentState = nextState
			transitionFlow.append(nextState)
		return currentState

	def isFinalState(self, someState):
		isFinal = False
		for state in self.finalStates:
			if someState == state:
				isFinal = True
		return isFinal


	def getNextTransition(self, currentState, letter):
		for t in self.transitions:
			t1 = t.split(" ")
			if t1[0] == currentState and t1[1] == letter :
				return t1[2]

					



