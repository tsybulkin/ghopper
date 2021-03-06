from params import *
import numpy as np
import eq_jumping



class Robot():
	def __init__(self,x=0.7, b=3.0):
		# th = a + b - g
		th = np.pi - np.arctan(z/Lb)
		xy2 = np.array([x + np.sqrt(z**2 + Lb**2), 0.]) # tail point
		xyh = xy2 + Lb/2 * np.array([np.cos(th), np.sin(th)])
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
		self.log = []
		

	def next_pos(self,tau):
		if self.metastate 	== "flying": 
			self.q += self.fly(tau)

		elif self.metastate 	== "jumping": 
			dq1 = self.jump(tau)
			q1 = self.q + dq1 * tau
			xy1, xy2 = get_head_n_tail(q1)
			if xy1[1] < 0. or xy2[1] < 0: print "head", xy1, "   tail:", xy2
			self.q = q1

			if self.q[3] < 0.1: self.metastate = "flying" 


	def jump(self, tau):
		C = np.array([
			eq_jumping.get_c1(self.q,self.dq),
			eq_jumping.get_c2(self.q,self.dq),
			eq_jumping.get_c3(self.q,self.dq)
			])
		D = - np.array([
			eq_jumping.get_d1(self.q, self.dq),
			eq_jumping.get_d2(self.q,self.dq),
			eq_jumping.get_d3(self.q,self.dq)
			])
		return self.dq + np.hstack([np.zeros(2),tau * np.linalg.inv(C).dot(D)])

	def fly(self,tau):
		return np.zeros(5)


def get_head_n_tail(q):
	x,y,a,b,g = q

	xyh = np.array([x,y]) + L*np.array([np.cos(a), np.sin(a)]) \
						+ L*np.array([np.cos(a+b), np.sin(a+b)])

	head = xyh + Lb/2 * np.array([np.cos(a+b-g), np.sin(a+b-g)])\
					+ z*np.array([-np.sin(a+b-g),np.cos(a+b-g)])
	tail = xyh - Lb/2 * np.array([np.cos(a+b-g), np.sin(a+b-g)])

	return head,tail




