class Shape:
	default_mass=1
	default_thita=0
	def init(self,points=[[0]],masses=[default_mass,default_mass],Thita=default_thita):
		dimension_error=0
		if(not type(points)==list):
			dimension_error=1
		elif(not type(masses)==list):
			dimension_error=2
		elif(not len(points)==len(masses)):
			dimension_error=3
		else:
			for i in points:
				if(not type(i)==list):
					dimension_error=4
					break
				if(len(i)==len(points[0])):
					dimension_error=5
					break
				for j in i:
					if(not(type(j)==float or type(j)==int)):
						dimension_error=6
						break
				if(not dimension_error):
					break
			for i in masses:
				if(not (type(i)==int or type(i)==float)):
					dimension_error=7
					break
				elif(i==0):
					dimension_error=8
					break
		if(dimension_error==1):
			raise "Points has to be a list of points."
		elif(dimension_error==2):
			raise "Masses has to be a list of masses."
		elif(dimension_error==3):
			raise "Number of points must be equal to the number of masses"
		elif(dimension_error==4):
			raise "Each point has to be a list of coordinates."
		elif(dimension_error==5):
			raise "Each point has to have the same dimensions."
		elif(dimension_error==6):
			raise "Each coordinate has to be a number."
		elif(dimension_error==7):
			raise "Each mass has to be a number."
		elif(dimension_error==8):
			raise "Mass of a point cannot be zero."
		else:
			self.points=points#Coordinates of each point
			self.masses=masses#Mass of each point
			self.Thita=Thita#Initial angle of rotation of shape
			self.COM=[0 for i in points[0]]
			self.net_mass=0#Total mass of body
			for i in range(len(points)):
				for j in range(len(points[0])):
					self.COM[j]+=points[i][j]*masses[i]#Adds the jth points mass*(value of coordinate in jth dimension) of ith point
				self.net_mass+=masses[i]#Adds mass of each point
			for i in range(len(COM)):
				self.COM[i]/=self.net_mass#Weighted average of coordinates
