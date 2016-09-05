from params import *
import numpy as np
import eq_jumping



class Robot():
	def __init__(self,x=1., b=2.9):
		# th = a + b - g
		th = np.pi - np.arctan(z/L)
		xy2 = np.array([x + np.sqrt(z**2 + L**2), 0.]) # tail point
		xyh = xy2 + L/2 * np.array([np.cos(th), np.sin(th)])
		d = L * np.sin(b) / np.sin(b/2) # distance from CoM to toe
		xyt = np.array([xyh[0] + np.sqrt(d**2 - xyh[1]**2), 0.])
		a = np.pi - np.arcsin(xyh[1]/d) - b/2

		self.q = np.array([
			xyt[0],
			xyt[1],
			a,
			b,
			a + b - th
			])
		self.dq = np.zeros(5)
		self.metastate = "jumping"
		
	def next_pos(self,tau):
		if metastate 	== "flying": self.fly(tau)
		elif metastate 	== "jumping": self.jump(tau)


	def jump(self, tau):
		C = np.array([
			eqs.get_c1(self.q,self.q_d,self.psi),
			eqs.get_c2(self.q,self.q_d,self.psi),
			])


