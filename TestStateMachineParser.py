import StateMachineParser
s = StateMachineParser.StateMachineParser("fsm.txt")
print "The states present in stateMachine are \n ", s.get_states()
print "The initial state of the stateMachine is \n", s.get_initial_state()
print "The final States of the stateMachine is are \n", s.get_final_states()
print "The alphabet in StateMachine are \n",s.get_alpha()
print "The Transitions in the stateMachine are \n", s.get_transitions()