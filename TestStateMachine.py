import StateMachine
s = StateMachine.StateMachine()
#print s.validateValues()
s.setInitialState("1")
finalstates = ["5"]
states = ["1","2","3","4","5"]
transitions = ["1 a 2","1 b 2","2 a 2","2 b 1","2 c 3","3 a 4","3 c 5","4 a 5","4 b 3"]
alphabet =["a","b","c"]
s.addFinalStates(finalstates)
s.addStates(states)
s.addAlphabet(alphabet)
s.addTransitions(transitions)
#print s.getInitialState()
#print s.validateValues()
#print "should come true ",s.isFinalState("6")
#print "should come false  ",s.isFinalState("8")
#print "should print 2 ::::",s.getNextTransition("1","x")
#print "start transition function,\ntrainsition ends at ", s.startTransition("abcc","1")
print "start statemachine : "
s.stateMachineStart("aaccc")