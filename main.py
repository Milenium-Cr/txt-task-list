import pickle

listfile = "list.data"

class User:
	def __init__(self):
		self.todolist = []
		self.perfomed = []
		
	def addtoList(self):
		print("Что вы хотите добавить в свой лист?")
		todo = input(">>> ")
		print("Вы написали:\n%s\nУверены?\ny/n" % todo)
		a = input()
		if a == "y":
			self.todolist.append(todo)
			print("Хотите добавить еще одну? y/n")
			a = input()
			if a == "y":
				self.addtoList()
			else:
				print()
		elif a == "n":
			print()
	
	def madeList(self):
		print("Какую задачу вы выполнили?")
		count = 0
		countList = []
		for i in self.todolist:
			count += 1
			countList.append(count)
			print("%(count)s. %(list)s" % {"count": count, "list": i})
		made = int(input(">>> "))
		if made in countList:
			made -= 1
			self.perfomed.append(self.todolist[made])
			del self.todolist[made]
			print("Готово!")
		elif made not in countList:
			print("Такого элемента в списке нет!")
	
	def delfromList(self):
		print("Какую задачу вы хотите удалить?")
		count = 0
		countList = []
		for i in self.todolist:
			count += 1
			countList.append(count)
			print("%(count)s. %(list)s" % {"count": count, "list": i})
		made = int(input(">>> "))
		if made in countList:
			made -= 1
			del self.todolist[made]
			print("Готово!")
			self.savedata()
		elif made not in countList:
			print("Такого злемента в списке нет!")
	
	def list(self):
		print("Невыполненые задачи:")
		if self.todolist == []:
			print("Отсутствуют.")
		else:
			count = 0
			countList = []
			for i in self.todolist:
				count += 1
				countList.append(count)
				print("%(count)s. %(list)s" % {"count": count, "list": i})
		
	def profile(self):
		print("Кол-во невыполненых задач: %s" % len(user.todolist))
		print("Кол-во выполненых задач: %s\n" % len(user.perfomed))
		
		print("\nВыполненые задачи:")
		count = 0
		countList = []
		for i in self.perfomed:
			count += 1
			countList.append(count)
			print("%(count)s. %(list)s" % {"count": count, "list": i})
			
	def savedata(self):
		f = open(listfile, 'wb')
		pickle.dump(self.todolist, f)
		f.close()
		print("Список успешно сохранен!\n")
	
	def loaddata(self):
		f = open(listfile, 'rb')
		loadedData = pickle.load(f)
		self.todolist = loadedData
		print("Список успешно загружен!\n")

print("Задачник")
user = User()

# основной цикл
while True:
	print("Выберите функцию:")
	print("1. Добавить задачу")
	print("2. Выполнить задачу")
	print("3. Удалить задачу")
	print("4. Список задач")
	print("5. Профиль пользователя")
	print("6. Сохранить/создать список")
	print("7. Загрузить список")
	print("8. Сохранить и выйти")
	act = int(input())
	
	if act == 1:
		user.addtoList()
	elif act == 2:
		user.madeList()
	elif act == 3:
		user.delfromList()
	elif act == 4:
		user.list()
	elif act == 5:
		user.profile()
	elif act == 6:
		user.savedata()
	elif act == 7:
		user.loaddata()
	elif act == 8:
		user.savedata()
		break
	else:
		break