import numpy as np
from bot import Robot
from show import show

def run(T):
	t = 0.
	bot = Robot()
	tau  = 0.0005

	while t < T:
		print bot.q
		bot.log.append(bot.q)
		
		bot.next_pos(tau)
		t += tau

	speedup = 0.1
	show('jump.html', bot.log, tau/speedup)

