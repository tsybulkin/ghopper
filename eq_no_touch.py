import numpy as np
from params import *


## -----  d/dt(dL/da.) - dL/da
def get_c1(q,dq):
	a,b,g = q
	da,db,dg = dq
	return np.array([
		I1 + 2*L**2*m1*cos(b) + 2*L**2*m1,
		I1 + L**2*m1*cos(b) + L**2*m1,
		-I1
		])

def get_d1(q,dq):
	a,b,g = q
	da,db,dg = dq
	return Gr*L*m1*cos(a + b) + Gr*L*m1*cos(a) \
		- 2*L**2*m1*sin(b)*da*db - L**2*m1*sin(b)*db**2


## -----  d/dt(dL/db.) - dL/db
def get_c2(q,dq):
	a,b,g = q
	da,db,dg = dq
	return np.array([
		I1 + L**2*m1*cos(b) + L**2*m1,
		I1 + L**2*m1,
		-I1
		])

def get_d2(q,dq):
	a,b,g = q
	da,db,dg = dq
	return Gr*L*m1*cos(a + b) + L**2*m1*sin(b)*da**2 + k*r**2*b


## -----  d/dt(dL/dg.) - dL/dg
def get_c3(q,dq):
	a,b,g = q
	da,db,dg = dq
	return np.array([
		-I1,
		-I1,
		I1
		])

def get_d3(q,dq):
	a,b,g = q
	da,db,dg = dq
	return

