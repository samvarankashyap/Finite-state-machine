class StateMachineParser:	
	def __init__(self,fp):
		self.fd = open(fp,"r")		
		self.fields = self.fd.readlines()		
		print self.fields
	
	def getAll(self):
		print self.getAlpha()
		print self.getTransitions()
		print self.getIntialState()
		print self.getFinalState()

	def getAlpha(self):
		return self.getFieldByName("alphabet")
	def getTransitions(self):
		#print self.filePath
		transList = []		
		for x in self.fields :
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
			
	def getFieldByName(self,fieldName):
		for line in self.fields:
			temp = line.split(":")
			#print temp
			category = temp[0].strip(" ")
			#print category
			if fieldName == category :
				return self.getFieldListByName(temp[1].strip(),"states")
			if fieldName == category :
				return temp[1].strip("\n")
			if temp[0] == category :
				return self.getFieldListByName(temp[1],"final")
			if temp[0] == category :
				return self.getFieldListByName(temp[1],"alphabet")
			if temp[0] == category :
				return self.getFieldListByName(temp[1],"states")
			
			
	def getFieldListByName(self,fieldString,fieldName):
		fieldList = []
		elements = fieldString.split(" ")
		for e in elements:
			e.strip("\n")
			fieldList.append(e)
		return fieldList



		