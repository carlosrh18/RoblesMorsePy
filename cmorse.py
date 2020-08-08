"""
Autor: Carlos Andres Robles
Github: github.com/carlosrh18
RoblesMorsePy v1.0

"""


import requests
import random
import time
import sys


#Diccionario de equivalencia en tiempos de duracion de dots y dashes de cada letra en morse, dots: 1 segundo, dashes: 3 segundos

morseDict = {'A':[1,3], 'B':[3,1,1,1], 'C':[1,3,1,3], 'D':[3,1,1], 'E':[1], 'F':[1,1,3,1], 'G':[3,3,1], 'H':[1,1,1,1], 'I':[1,1],
 'J':[3,1,1,1], 'K':[3,1,3],'L': [1,3,1,1], 'M':[3,3], 'N':[3,1], 'O':[3,3,3], 'P':[1,3,3,1], 'Q':[3,3,1,3], 'R':[1,3,1], 'S':[1,1,1],
 'T':[3], 'U':[1,1,3], 'V':[1,1,1,3], 'W':[1,3,3], 'X': [3,1,1,3], 'Y':[3,1,3,3], 'Z':[3,3,1,1]}


class Morser(object):
	"""

	RoblesMorserPy v1.0

	*** Recuerda instalar Ip Webcam para android ****

	Siempre usar el puerto 8080

	Modo de uso (como Modulo):

	>>> morser = Morser('palabra')
	>>> morser.MkWord('192.168.1.18')

	Modo de uso como ejecutable

	>>> python RoblesMorsePy.py SOS 192.168.1.18


	"""
	def __init__(self,word):
		self.word = word

	def Splitw(self):
		self.word
		return [c for c in self.word]
	#letter to morse conversion and emits the flash light
	def CharMorse(self,char,ipDir):
		char = char.upper()
		times =  morseDict[char]
		print(times)
		try:
			for i in times:
				requests.get(f'http://{ipDir}:8080/enabletorch')
				time.sleep(i)
				requests.get(f'http://{ipDir}:8080/disabletorch')
				time.sleep(1)
				print(i)
			pass

		except IndexError as error:
			print(error)

		except Exception as e:
			print(e)

	def MkWord(self,ipDir):
		flagArr = self.Splitw()
		for c in flagArr:
			print(c)
			self.CharMorse(c,ipDir)
			time.sleep(3)


'''
while True: #Run forever
	requests.get('http://192.168.1.18:8080/enabletorch')
	time.sleep(1)
	requests.get('http://192.168.1.18:8080/disabletorch')
	time.sleep(1)
	
'''


if __name__ == "__main__":
	str = sys.argv[1]
	ip_Dir = sys.argv[2]
	m = Morser(str)
	print(m.Splitw())
	m.MkWord(ip_Dir)

