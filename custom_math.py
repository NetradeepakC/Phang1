"""
Equation: a1*x1+a2*x2+......an*xn=b
Given n equations,
they are solved by the following recursive method
the following set of equations
a1*X11+a2*X12+......an*X1n=b1
a1*X21+a2*X22+......an*X2n=b2
.
.
.
an*Xn1+a2*Xn2+......an*Xnn=bn

becomes,

a2(X22-X12*X21/X11)+a3(X23-X13*X21/X11)+......an(X2n-X1n*X21/X11)=b2-b1*X21/X11
a2(X32-X12*X31/X11)+a3(X33-X13*X31/X11)+......an(X3n-X1n*X31/X11)=b3-b1*X31/X11
.
.
.
a2(Xn2-X12*Xn1/X11)+a3(Xn3-X13*Xn1/X11)+......an(Xnn-X1n*Xn1/X11)=b2-b1*Xn1/X11
"""
class equation:
	def __init__(self,coefficients,value):
		self.coefficients=coefficients
		self.value=value
def solve_equations(equations):
	if(len(equations)==1):
		return [equations[0].value/equations[0].coefficients[0]]
	else:
		coefficients=[[equations[i].coefficients[j]-equations[0].coefficients[j]*equations[i].coefficients[0]/coefficients[0].equations[0] for j in range(1,len(equations[0].coefficients))] for i in range(1,len(equations))]
		value=[equations[i].value-equations[0].value*equations[i].coefficients[0]/equations[0].coefficients[0] for i in range(1,len(equations))]
		variables=solve_equations([equation(coefficients[i],value[i]) for i in range(len(equations)-1)])
		a0=equations[0].value
		for i in range(1,len(equations[0].coefficients)):
			a0-=variables[i]*equations[0].coefficients[i]
		a0/=equations[0].coefficients[0]
		return [a0]+variables
