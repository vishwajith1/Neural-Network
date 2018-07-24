#!/usr/bin/env python3


import sys
import math

class network:

	def __init__(self, layer, input):
		self.layer = list()
		self.input = list()
		
		self.temp = list()
		a = 0
		l = len(layer) - 1
		layer_length = int(layer[l][0])
		layer_length = layer_length + 1
	
		for i in range(layer_length):
			self.temp = []
			for j in layer:
				if int(j[0]) == a:
					self.temp.append(j)
			
			new = rlayer(self.temp)
			self.layer.append(new)		
			a = a + 1
				
		for j in input:
			for i in range(1, len(j)):
				self.input.append(float(j[i]))
		self.output()
		 
	
		
	def output(self):
		for i in self.layer:
			result = i.loutput(self.input)
			self.input = []
			for i in result:
				self.input.append(i)
				#print(i)	
		
		for i in self.input:
			print(i)	
			 
class rlayer:

	def __init__(self, layer):
		self.neuron = list()
		for i in layer:
			new = rneuron(i)
			self.neuron.append(new)
	
	def loutput(self, input):
		self.output = list()
		for i in self.neuron:	
			result = i.neoutput(input)
			self.output.append(result)
		return self.output

class rneuron:
	def __init__(self, n):		
		self.neuron = list()
		self.weight = list()
		self.bias = 0.00
		l = len(n) - 1
		for i in range(2,l):
			w = float(n[i])
			self.weight.append(w)	
		self.bias = float(n[l])
		
		
			
	
	def neoutput(self, input):
		value = 0.00
		l = len(self.weight) 
		#print("weight -- "+str(self.weight))
		#print("input --"+str(input))
		for i in range(l):
			value = value + self.weight[i] * input[i]
			
		output = 1/(1+math.exp(-(self.bias + value)))
		#self.output.append(output)			
		return output				
				
		
def main():

	file = open(sys.argv[1], 'r')
	info=file.read().splitlines()
	file.close()
        
	x = list()
	for d in info:
		d = d.split("#")[0]
		d = d.strip()
		d = d.split()	
		x.append(d)	
	layer = list()
	input = list()
	for i in x:
		if len(i) != 0 and i[0] != 'inputs':
			layer.append(i)
		elif len(i) != 0 and i[0] == 'inputs':
			input.append(i)
		
	n = network(layer, input)
	#n._init_(layer, input)	
	#frint(x)
	#print(layer)
	#print(input)

main()
