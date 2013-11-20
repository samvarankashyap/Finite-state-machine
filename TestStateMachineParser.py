import StateMachineParser
s = StateMachineParser.StateMachineParser("fsm.txt")
print "The states present in stateMachine are \n ", s.getStates()
print "The initial state of the stateMachine is \n", s.getInitialState()
print "The final States of the stateMachine is are \n", s.getFinalState()
print "The alphabet in StateMachine are \n",s.getAlpha()
print "The Transitions in the stateMachine are \n", s.getTransitions()