import StateMachine
import StateMachineParser

class FiniteStateMachine:
	def __init__(self,file_path):
		self.file_path=file_path

	def create_object(self):
		sm = StateMachine.StateMachine()
		smp = StateMachineParser.StateMachineParser(self.file_path)
		initial_state = smp.get_initial_state()
		final_states = smp.get_final_states()
		alphabet = smp.get_alpha()
		transitions = smp.get_transitions()
		states = smp.get_states()
		sm.set_initial_state(initial_state)
		sm.add_final_states(final_states)
		sm.add_states(states)
		sm.add_alphabet(alphabet)
		sm.add_transitions(transitions)
		return sm


