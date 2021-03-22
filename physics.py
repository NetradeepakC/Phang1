def update_kinematics(point_object,force=[0,0,0],time_step=1/60,values={}):
	
	acceleration=[]
	if(type(force[0])==int):
		for i in force:
			acceleration.append(i/point_object.mass)
	else:
		values["body_mass"]=point_object.mass
		values["body_charge"]=point_object.charge
		for i in range(len(point_object.position)):
			values["coordinate"+str(i)]=point_object.position[i]
			values["axial_velocity"+str(i)]=point_object.velocity[i]
		for i in force:
			acceleration.append(i.evaluate_equation(values)/point_object.mass)
	for i in range(len(acceleration)):
		point_object.velocity[i]+=acceleration[i]*time_step
		point_object.position[i]+=point_object.velocity[i]*time_step
