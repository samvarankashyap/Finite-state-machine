import StateMachine
s = StateMachine.StateMachine()
print s.validateValues()
s.setInitialState("1")
finalstates = ["6"]
states = ["1","2","3","4","5"]
transitions = ["1a2","1b2","2a2","2b1","2c3","3a4","3c5","4a5","4b3"]
alphabet =["a","b","c"]
s.addFinalStates(finalstates)
s.addStates(states)
s.addAlphabet(alphabet)
s.addTransitions(transitions)
print s.getInitialState()
print s.validateValues()
print "should come true ",s.isFinalState("6")
print "should come false  ",s.isFinalState("8")
print "should print 2 ::::",s.getNextTransition("1","x")

print "start transition function, trainsition ends at ", s.startTransition("xc","1")