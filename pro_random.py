#1 importing modules
'''import random
for e in range(7):
	print(random.randint(1,10))'''
	
#2
import sys
while True:
	print("type exit to exit.")
	response=input()
	if response=="exit":
		sys.exit()
	print("you typed"+response+("."))
	