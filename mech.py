from sympy import cos, sin, diff, symbols
from sympy.physics.mechanics import LagrangesMethod, dynamicsymbols


def init_no_touch(): return dynamicsymbols('a b g')

def Ln(a,b,g):
	
	xt,yt,Gr,m1,Lb,L,I1,z,r,k = \
	symbols('xt yt Gr m1 Lb L I1 z r k')

	da, db, dg = dynamicsymbols('a b g',1)

	xc = xt + L*(cos(a) + cos(a+b))
	yc = yt + L*(sin(a) + sin(a+b))

	T = m1/2*(xc.diff('t')**2 + yc.diff('t')**2) + I1/2*(da+db-dg)**2 
	V = m1*Gr*yc + k/2*(r*b)**2 

	return T-V

