import FiniteStateMachine

fsm = FiniteStateMachine.FiniteStateMachine("fsm.txt")
stateMachineObject = fsm.create_object()
stateMachineObject.state_machine_start("aac")