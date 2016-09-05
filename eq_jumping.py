import numpy as np
from params import *


## -----  d/dt(dL/da.) - dL/da
def get_c1(q,dq):
	_,_,a,b,g = q
	_,_,da,db,dg = dq
	return np.array([
		I1 + 2*L**2*m1*np.cos(b) + 2*L**2*m1,
		I1 + L**2*m1*np.cos(b) + L**2*m1,
		-I1
		])

def get_d1(q,dq):
	_,_,a,b,g = q
	_,_,da,db,dg = dq
	return Gr*L*m1*np.cos(a + b) + Gr*L*m1*np.cos(a) \
		- 2*L**2*m1*np.sin(b)*da*db - L**2*m1*np.sin(b)*db**2


## -----  d/dt(dL/db.) - dL/db
def get_c2(q,dq):
	_,_,a,b,g = q
	_,_,da,db,dg = dq
	return np.array([
		I1 + L**2*m1*np.cos(b) + L**2*m1,
		I1 + L**2*m1,
		-I1
		])

def get_d2(q,dq):
	_,_,a,b,g = q
	_,_,da,db,dg = dq
	return Gr*L*m1*np.cos(a + b) + L**2*m1*np.sin(b)*da**2 + k*r**2*b


## -----  d/dt(dL/dg.) - dL/dg
def get_c3(q,dq):
	_,_,a,b,g = q
	_,_,da,db,dg = dq
	return np.array([
		-I1,
		-I1,
		I1
		])

def get_d3(q,dq):
	_,_,a,b,g = q
	_,_,da,db,dg = dq
	return 0.

