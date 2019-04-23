class stackFull(Exception):
	pass

class stackEmpty(Exception):
	pass

class Stack:
	"""Class implementing stack using list"""
	def __init__(self,n):
		self.__stack = [None]*n
		self.__size  = 0
		self.__current = -1 
	
	def get_current(self):
		print('C:{}'.format(self.__current))
	
	#Implementing push function
	def push(self,value):
		if self.is_full():
			raise stackFull
		else:
			self.__current = self.__current+1
			self.__stack[self.__current] = value
			self.__size = self.__size+1
	
	
	#Implementing pop function
	def pop(self):
		if self.is_empty():
			raise stackEmpty
		else:
			self.__stack[self.__current]= None
			self.__size = self.__size - 1
			self.__current = self.__current - 1

	#Implementing is_full function
	def is_full(self):
		if self.__current == (len(self.__stack)-1):
			return True 
		else:
			return False

	#Implelenting is_empty function
	def is_empty(self):
		if self.__size==0:
			return True
		else:
			return False

	#Implementing length function
	def __len__(self):
		return self.__size

	#Implementing print function
	def __str__(self):
		return(' '.join([str(self.__stack[a]) for a in range(0,self.__size) ]))

if __name__ == '__main__':

	try:	
		obj = Stack(5)
		print(obj.is_empty())
		print(obj.is_full())
		obj.push(5)
		print(obj)
		obj.push(8)
		print(obj)
		obj.push(9)
		print(obj)
		obj.pop()
		print(obj)
		obj.pop()
		print(obj)
		obj.push(10)
		print(obj)
		obj.push(10)
		print(obj)
		obj.push(10)
		print(obj)
		obj.pop()
		print(obj)
		obj.pop()
		print(obj)
		obj.pop()
		print(obj)
		obj.pop()
		print(obj)
		obj.pop()
		print(obj)
	except stackFull as e:
		print("stackfull")
	except stackEmpty as e:
		print("stackempty")
