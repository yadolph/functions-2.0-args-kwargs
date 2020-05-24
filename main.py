

class Contact:

	def __init__(self, first_name, last_name, phone_num, fav=False, **kwargs):
		self.first_name = first_name
		self.last_name = last_name
		self.phone_num = phone_num
		self.fav = fav
		self.kwargs = kwargs

	def __str__(self):

		fname = f'Имя: {self.first_name}\n'
		lname = f'Фамилия: {self.last_name}\n'
		phnum = f'Телефон: {self.phone_num}\n'
		if self.fav == True:
			infav = 'В избранных: да \n'
		else:
			infav = 'В избранных: нет \n'

		add_info = ''

		if self.kwargs:
			add_info = 'Дополнительная информация: \n'
			for key, val in self.kwargs.items():
				add_info += f'    {key} : {val}\n'

		return fname + lname + phnum + infav + add_info

class PhoneBook:

	def __init__(self, name, *args, **kwargs):
		



john = Contact('John', 'Doe', '+88005553535', telegram='@johnny2000', email='johnny@yahoo.com')

print(john)

