from api import API
import random

while(1):
	a=API()
	_device=random.randint(1,2)
	a.setDevice(_device)
	a.reroll(True)
	exit(1)