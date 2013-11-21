class StateMachine:
	

	def __init__(self):
		self.initialState = []
		self.finalStates = []
		self.states = []
		self.alphabet = []
		self.transitions = []

	def set_initial_state(self, initialState):
		self.initialState = initialState
		
	def add_final_states(self, finalStates):
		self.__addListTo(finalStates, "finalStates")
		
	def add_states(self, states):
		self.__addListTo(states, "states")
		
	def add_alphabet(self, alphabet):
		self.__addListTo(alphabet, "alphabet")

	def add_transitions(self, transitions):
		self.__addListTo(transitions, "transitions")
		
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
		else:
			for temp in list:
				(self.transitions).append(temp)

	def get_initial_state(self):
		return self.initialState[0]

	def state_machine_start(self, inputString): 
		#starting the state machine with the input string
		if(self.validate_values()): #verifies whether the object is properly intialised or not 
			currentState = self.get_initial_state() # stores initial state 
			finalTransitionState = self.start_transition(inputString, currentState) #  should give final transtition state 
			if(self.is_final_state(finalTransitionState)): #checking whether the final state reached is in set of final states or not
				print "Final State Reached ... Transition stopped at "+finalTransitionState
			else: 
				print "Invalid String Transition stopped at "+str(finalTransitionState)
		else:
			print "object values are not initialised properly ....."

	def validate_values(self):
		if(len(self.initialState) == 0 or len(self.alphabet) == 0 or len(self.transitions) == 0):
			return False
		else :
			return True
 
	def start_transition(self, inputString, currentState):
		transitionFlow = []
		transitionFlow.append(self.get_initial_state())
		for c in inputString:
			nextState = self.get_next_transition(currentState,c)
			if(nextState == None):
				return transitionFlow[-1]
			currentState = nextState
			transitionFlow.append(nextState)
		return currentState

	def is_final_state(self, someState):
		isFinal = False
		for state in self.finalStates:
			if someState == state:
				isFinal = True
		return isFinal

	def get_next_transition(self, currentState, letter):
		for t in self.transitions:
			t1 = t.split(" ")
			if(t1[0] == currentState and t1[1] == letter):
				return t1[2]

					



