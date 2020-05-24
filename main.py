import datetime


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
		self.name = name
		self.args = args
		self.kwargs = kwargs
		self.contact_list = []

	def create_new_contact(self, first_name, last_name, phone_num, fav = False, **kwargs):
		self.contact_list.append(Contact(first_name, last_name, phone_num, fav, **kwargs))

	def list_all_contacts(self):
		curr_time = datetime.datetime.now()
		num_of_contacts = len(self.contact_list)
		print(f'В телефонной книге "{self.name}" {num_of_contacts} контакт(a/ов) по состоянию на {curr_time}:')
		for contact in self.contact_list:
			print(contact)

	def del_con_by_phone_num(self, phone_num_to_del):
		for contact in self.contact_list:
			if contact.phone_num == phone_num_to_del:
				print(f'Контакт с номером {phone_num_to_del} ({contact.first_name} {contact.last_name}) удален\n')
				self.contact_list.remove(contact)

	def list_all_fav_contacts(self):
		fav_contact_list = []
		for contact in self.contact_list:
			if contact.fav == True:
				fav_contact_list.append(contact)
		curr_time = datetime.datetime.now()
		if fav_contact_list:
			print(f'В телефонной книге "{self.name}" {len(fav_contact_list)} избранный(ых) контакт(а/ов) по состоянию на {curr_time}')
			for contact in fav_contact_list:
				print(contact)
		else:
			print('В вашей телефонной книге нет избранных контактов')

	def search_by_name(self, first_name, last_name):
		for contact in self.contact_list:
			if contact.first_name == first_name and contact.last_name == last_name:
				print('Найден контакт с указанным именем и фамилией: ')
				print(contact)


my_book = PhoneBook('Main Book')

my_book.create_new_contact('John', 'Doe', '+88005553535', telegram='@johnny2000', email='johnny@yahoo.com')
my_book.create_new_contact('Vasya', 'Pupkin', '+88001111111', instagram='@pupkin_real', email='vasya@pupkin.com')
my_book.create_new_contact('Lady', 'Gaga', '+1234567890', fav=True, twitter='@ladygaga')

my_book.list_all_contacts()

my_book.del_con_by_phone_num('+88005553535')

my_book.list_all_contacts()

my_book.list_all_fav_contacts()

my_book.search_by_name('Vasya', 'Pupkin')