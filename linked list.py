import sys
class Node:
	def __init__(self,value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.top = None
		self.current = None

	def add(self,value):
		obj = Node(value)
		if self.top == None:
			self.top = obj
			self.current = obj
		else:
			if self.top.next == None:
				self.top.next == obj
			self.current.next = obj
			self.current = obj

	def delete(self,value):
		temp = self.top
		previous = None
		while(temp != None):
			if temp.value == value:
				if previous != None:
					previous.next = temp.next
				else:
					self.top = temp.next

				if self.current.value == value:
					self.current = previous
				return
			previous = temp
			temp= temp.next
		print("Element not found")

	def insert(self,value,before):
		temp = self.top
		while(temp != None):
			obj = Node(value)
			if temp.value == before:
				obj.next = temp.next
				temp.next = obj
				if obj.next == None:
					self.current = obj
				return 
			temp = temp.next
		print("Element not found")


	def show(self):
		temp = self.top
		while temp != None:
			print(temp.value)
			temp=temp.next
		print("------------------------------------")

if __name__ == '__main__':
	print(sys.executable)
	l = LinkedList()
	l.add(5)
	l.add(3)
	l.add(4)
	l.show()
	l.delete(4)
	l.delete(5)
	l.show()
	l.add(5)
	l.show()
	l.add(8)
	l.show()
	l.insert(4,8)
	l.show()




