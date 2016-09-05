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
		if metastate 	== "flying": 
			self.q += self.fly(tau)

		elif metastate 	== "jumping": 
			dq1 = self.jump(tau)
			self.q += dq1
			if self.q[3] < 0.1: self.metastate = "flying" 


	def jump(self, tau):
		C = np.array([
			eq-jumping.get_c1(self.q,self.dq),
			eq-jumping.get_c2(self.q,self.dq),
			eq-jumping.get_c3(self.q,self.dq)
			])
		D = - np.array([
			eq-jumping.get_d1(self.q, self.dq),
			eq-jumping.get_d2(self.q,self.dq),
			eq-jumping.get_d3(self.q,self.dq)
			])
		return self.dq + np.hstack([np.zeros(2),tau * np.linalg.inv(C).dot(D)])

	def fly(self,tau):
		return np.zeros(5)

