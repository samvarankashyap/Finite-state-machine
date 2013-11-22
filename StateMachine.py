from exceptions import Exception
import re

class InvalidStateException(Exception):
	def __init__(self, msg):
		Exception.__init__(self, msg)

class DuplicateStateException(Exception):
	def __init__(self, msg):
		Exception.__init__(self, msg)

class StateMachine:
	

	def __init__(self):
		self.initial_state = ""
		self.final_states = []
		self.states = []
		self.alphabet = []
		self.transitions = []

	def set_initial_state(self, initial_state):
		initial_state = initial_state.strip()
		#print initial_state
		if (self.is_valid_state(initial_state)):
			raise InvalidStateException("This is Invalid state")
		else:
			self.initial_state = initial_state
	
	def add_state(self,single_state):
		single_state = str(single_state)
		single_state = single_state.strip()
		#print self.states
		#print self.does_state_exists(single_state,"states")
		
		if (self.does_state_exists(single_state,"states")):
			raise DuplicateStateException("This is a DuplicateStateException")
		
		if self.is_valid_state(single_state):
			raise InvalidStateException("This is an Invalid state ")
					
		self.states.append(single_state)
		
	def add_states(self,*args):
		args_list = self.args_to_list(args)
		for a in args_list:
			self.add_state(a)
		
	def add_final_states(self, final_states):
		self.__addListTo(final_states, "final_states")
		
	#def add_states(self, states):
	#	self.__addListTo(states, "states")
		
	def add_alphabet(self, alphabet):
		self.__addListTo(alphabet, "alphabet")

	def add_transitions(self, transitions):
		self.__addListTo(transitions, "transitions")
		
	def __addListTo(self, list, nameOfList):
		if nameOfList == "final_states":
			for temp in list:
				(self.final_states).append(temp)
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
		return self.initial_state

	def state_machine_start(self, input_string): 
		#starting the state machine with the input string
		if(self.validate_values()): #verifies whether the object is properly intialised or not 
			current_state = self.get_initial_state() # stores initial state 
			finalTransitionState = self.start_transition(input_string, current_state) #  should give final transtition state 
			if(self.is_final_state(finalTransitionState)): #checking whether the final state reached is in set of final states or not
				print "Final State Reached ... Transition stopped at "+finalTransitionState
			else: 
				print "Invalid String Transition stopped at "+str(finalTransitionState)
		else:
			print "object values are not initialised properly ....."

	def validate_values(self):
		if(len(self.initial_state) == 0 or len(self.alphabet) == 0 or len(self.transitions) == 0):
			return False
		else :
			return True
 
	def start_transition(self, input_string, current_state):
		transitionFlow = []
		transitionFlow.append(self.get_initial_state())
		for c in input_string:
			nextState = self.get_next_transition(current_state,c)
			if(nextState == None):
				return transitionFlow[-1]
			current_state = nextState
			transitionFlow.append(nextState)
		return current_state

	def is_final_state(self, some_state):
		is_final = False
		for state in self.final_states:
			if some_state == state:
				is_final = True
		return is_final

	def get_next_transition(self, current_state, letter):
		for t in self.transitions:
			t1 = t.split(" ")
			if(t1[0] == current_state and t1[1] == letter):
				return t1[2]

	def is_valid_state(self,some_state):
		
		if (some_state.isspace() or some_state=="" or (" " in some_state) or  self.match_valid(some_state) ):
			return True
		else:
			return False
	def match_valid(self,string):
		if (re.match("^[a-zA-Z0-9_]+",string)== None ):
			return True
		else:
			return False

	def change_args_to_list(self,args):
		l = []
		for c in args:
			l.append(c)
		return l

	def does_state_exists(self,state,field_name):
		if field_name == "states":
			if state in self.states:
				return True
			else:
				return False
		if field_name == "initial":
			if state in self.initial_state:
				return True
			else:
				return False
		if field_name == "final":
			if state in self.final_states:
				return True
			else:
				return False
		if field_name == "alphabet":
			if state in self.alphabet:
				return True
			else:
				return False
		if field_name == "transtition":
			if state in transtitions:
				return True
			else:
				return False


	def args_to_list(self,args):
		l1 = []
		for a in args:
			l1.append(a)
		return l1
					
		
		



					



