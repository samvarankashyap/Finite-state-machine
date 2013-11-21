

class StateMachineParser:	
	

	def __init__(self, file_path):
		self.file_descriptor = open(file_path,"r")		
		self.fields = self.file_descriptor.readlines()		
		#print self.fields
	
	def get_all(self):
		print self.get_alpha()
		print self.get_transitions()
		print self.getIntialState()
		print self.get_final_state()

	def get_alpha(self):
		return self.get_field_by_name("alphabet")
	
	def get_transitions(self):
		transList = []		
		for x in self.fields:
			x1= x.split(":")
			if (x1[0].strip()=="transition"):
				transList.append(x1[1].strip())
		return transList
	
	def get_states(self):
		return self.get_field_by_name("states")
	
	def get_initial_state(self):
		return self.get_field_by_name("initial")
		
	def get_final_states(self):
		return self.get_field_by_name("final")
			
	def get_field_by_name(self, fieldName):
		for line in self.fields:
			temp = line.split(":")
			category = temp[0].strip(" ")
			if fieldName == category:
				return self.get_field_list_by_name(temp[1].strip(),fieldName)

			
	def get_field_list_by_name(self, fieldString, fieldName):
		fieldList = []
		elements = fieldString.split(" ")
		for e in elements:
			e.strip("\n")
			fieldList.append(e)
		return fieldList



		