import requests
import random
import time
import sys

on  = requests.get('http://192.168.1.18:8080/enabletorch')
off = requests.get('http://192.168.1.18:8080/disabletorch')
toggle = requests.get('http://192.168.1.18:8080/toggletorch')

morseDict = {'A':[1,3], 'B':[3,1,1,1], 'C':[1,3,1,3], 'D':[3,1,1], 'E':[1], 'F':[1,1,3,1], 'G':[3,3,1], 'H':[1,1,1,1], 'I':[1,1],
 'J':[3,1,1,1], 'K':[3,1,3],'L': [1,3,1,1], 'M':[3,3], 'N':[3,1], 'O':[1,1,1], 'P':[1,3,3,1], 'Q':[3,3,1,3], 'R':[1,3,1], 'S':[1,1,1],
 'T':[3], 'U':[1,1,3], 'V':[1,1,1,3], 'W':[1,3,3], 'X': [3,1,1,3], 'Y':[3,1,3,3], 'Z':[3,3,1,1]}


class Morser(object):
	def __init__(self,word):
		self.word = word

	def Splitw(self):
		self.w = self.word
		return [c for c in self.w]
	#letter to morse conversion and emits the flash light
	def CharMorse(self,char):
		char = char.upper()
		times =  morseDict[char]
		print(times)
		try:
			for i in times:
				requests.get('http://192.168.1.18:8080/enabletorch')
				time.sleep(i)
				requests.get('http://192.168.1.18:8080/disabletorch')
				time.sleep(1)
				print(i)
			pass

		except IndexError as error:
			print(error)

		except Exception as e:
			print(e)

	def MkWord(self):
		flagArr = self.Splitw(self.word)
		for c in flagArr:
			time.sleep(3)
			CharMorse(c)
'''
while True: #Run forever
	requests.get('http://192.168.1.18:8080/enabletorch')
	time.sleep(1)
	requests.get('http://192.168.1.18:8080/disabletorch')
	time.sleep(1)
	print('tic')
'''


if __name__ == "__main__":
	str = sys.argv[1]
	m = Morser(str)
	print(m.Splitw())
	m.CharMorse('c')

