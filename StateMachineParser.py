

class StateMachineParser:	
	

	def __init__(self, file_path):
		self.file_descriptor = open(file_path,"r")		
		self.fields = self.file_descriptor.readlines()		
		#print self.fields
	
	def getAll(self):
		print self.getAlpha()
		print self.getTransitions()
		print self.getIntialState()
		print self.getFinalState()

	def getAlpha(self):
		return self.getFieldByName("alphabet")
	
	def getTransitions(self):
		transList = []		
		for x in self.fields:
			x1= x.split(":")
			if (x1[0].strip()=="transition"):
				transList.append(x1[1].strip())
		return transList
	
	def getStates(self):
		return self.getFieldByName("states")
	
	def getInitialState(self):
		return self.getFieldByName("initial")
		
	def getFinalState(self):
		return self.getFieldByName("final")
			
	def getFieldByName(self, fieldName):
		for line in self.fields:
			temp = line.split(":")
			category = temp[0].strip(" ")
			if fieldName == category:
				return self.getFieldListByName(temp[1].strip(),fieldName)

			
	def getFieldListByName(self, fieldString, fieldName):
		fieldList = []
		elements = fieldString.split(" ")
		for e in elements:
			e.strip("\n")
			fieldList.append(e)
		return fieldList



		