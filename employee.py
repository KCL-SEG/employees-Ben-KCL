"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
	def __init__(self, name: str, salary: int, hours: int = 0, commission: int = 0, contracts: int = 0, bonus: int = 0):
		self.name = name
		self.salary = salary
		self.hours = hours
		self.commission = commission
		self.contracts = contracts
		self.bonus = bonus

	def get_commission(self):
		if self.commission: return self.commission * self.contracts
		elif self.bonus: return self.bonus
		else: return 0

	def get_pay_for_time(self):
		if self.hours: return self.hours * self.salary
		else: return self.salary

	def get_pay(self):
		return self.get_pay_for_time() + self.get_commission()

	def commission_string(self):
		contract = f' and receives a commission for {self.contracts} contract(s) at {self.commission}/contract'
		bonus = f' and receives a bonus commission of {self.bonus}'

		if not(self.commission or self.bonus): return ''
		elif self.commission: return contract
		else: return bonus

	def __str__(self):
		start = f'{self.name} works on a '
		commission = self.commission_string()
		type = f'monthly salary of {self.salary}{commission}. ' if not self.hours else f'contract of {self.hours} hours at {self.salary}/hour{commission}. '
		total = f' Their total pay is {self.get_pay()}.'
		return start + type + total


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', salary=25, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, commission=200, contracts=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', salary=25, hours=150, commission=220, contracts=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', salary=30, hours=120, bonus=600)
