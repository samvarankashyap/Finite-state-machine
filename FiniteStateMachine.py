import StateMachine
import StateMachineParser

class FiniteStateMachine:
	def __init__(self,filePath):
		self.filePath=filePath

	def create_object(self):
		sm = StateMachine.StateMachine()
		smp = StateMachineParser.StateMachineParser(self.filePath)
		initialstate = smp.get_initial_state()
		finalstates = smp.get_final_states()
		alphabet = smp.get_alpha()
		transitions = smp.get_transitions()
		states = smp.get_states()
		sm.set_initial_state(initialstate)
		sm.add_final_states(finalstates)
		sm.add_states(states)
		sm.add_alphabet(alphabet)
		sm.add_transitions(transitions)
		return sm


