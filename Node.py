class Connector:
	def __init__(self,owner, name, activates=0, monitor=0):
		self.value = None
		self.owner = owner
		self.name = name
		self.monitor = monitor
		self.connects = []
		self.activates = activates


	def connect(self, inputs):
		if type(inputs) != type([]):
			inputs = [inputs]
		for input in inputs:
			self.connects.append(input)

	def set(self, value):
		if self.value == value:
			return

		self.value = value

		if self.activates:
			self.owner.evaluate()

		for con in self.connects:
			con.set(value)


class LC:
	def __init__(self, name = "temp"):
		self.name = name

	def evaluate():
		return


class Not(LC):
	def __init__(self, name):
		LC.__init__(self, name)
		self.input1 = Connector(self, 'A', activates=1)
		self.output = Connector(self,'B')

	def evaluate(self):
		self.output.set(not self.input1.value)

class Gate2(LC):
	def __init__(self,name):
		LC.__init__(self, name)
		self.input1 = Connector(self, 'A', activates = 1)
		self.input2 = Connector(self, 'B', activates = 1)
		self.output = Connector(self, 'C')


class And(Gate2):
	def __init__(self, name):
		Gate2.__init__(self, name)

	def evaluate(self):
		self.output.set(self.input1.value and self.input2.value)

class Or(Gate2):
	def __init__(self, name):
		Gate2.__init__(self, name)

	def evaluate(self):
		self.output.set(self.input1.value or self.input2.value)