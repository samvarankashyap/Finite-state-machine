import StateMachine
s = StateMachine.StateMachine()
s.setInitialState("1")
finalstates = ["5"]
states = ["1","2","3","4","5"]
transitions = ["1 a 2","1 b 2","2 a 2","2 b 1","2 c 3","3 a 4","3 c 5","4 a 5","4 b 3"]
alphabet =["a","b","c"]
s.addFinalStates(finalstates)
s.addStates(states)
s.addAlphabet(alphabet)
s.addTransitions(transitions)
print "start statemachine : "
s.stateMachineStart("aaccc")