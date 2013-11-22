from exceptions import Exception



   	def setId(self, val):
    	val = val.strip()
    	if hasattr(self, 'nodeId'):
    		raise MultipleNodeIdException('Cannot define multiple values for the same node Id')
    	if (val == ''):
    		raise InvalidNodeIdException("Empty string cannot be used as a node ID")