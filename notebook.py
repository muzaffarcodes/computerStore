import sqlite3
import time

contact = sqlite3.connect("/home/muzaffar/Desktop/Python_Files/notebookStore.db")

index = contact.cursor()

def enter_table():
	index.execute("CREATE TABLE IF NOT EXISTS notebookStore (Company Text, Model Text, RAM Text, Price Text)")
	contact.commit()

enter_table()

def data_qosh(comp,model,ram,price):
	index.execute("INSERT INTO notebookStore VALUES(?,?,?,?)",(comp,model,ram,price))
	contact.commit()

def data_olibKel():
	index.execute("SELECT * FROM notebookStore")
	info = index.fetchall()
	print("Sabr...")
	time.sleep(2)
	for i in info:
		print(i)


def data_yangilaNarx():
	index.execute("UPDATE notebookStore SET Price=? WHERE Model=?",(input("Yangi Narx: "),input("Qaysi modelniki: "),))
	contact.commit()

def data_yangilaModel():
	index.execute("UPDATE notebookStore SET Model=? WHERE Company=?",(input("Yangi Model: "),input("Qaysi Kompaniyanikini: "),))
	contact.commit()

def data_yangilaRAM():
	index.execute("UPDATE notebookStore SET RAM=? WHERE Company=?",(input("Yangi RAM: "),input("Qaysi Kompaniyanikini: "),))
	contact.commit()

def data_ochir1():
	index.execute("DELETE FROM notebookStore WHERE Company=?",(input("Notebook nomi:"),))
	contact.commit()

def data_ochirHammasini():
	index.execute("DELETE FROM notebookStore")
	contact.commit()

while True:
	tanlov = int(input("""

~ASAXIY.UZ~

1. Ma'lumotlar qo'shish
2. Notebooklarni ko'rish
3. Ma'lumotlarni o'zgartirish
4. 1 malumotni o'chirish
5. Hammasini o'chirish
0. Chiqish eshiklari:)

Tanlange: """))	
	if tanlov == 1:
		comp = input("Notebook nomi: ")
		model = input("MOdel Nomi: ")
		ram = input("RAM: ")
		price = input("Narx: ")
	elif tanlov == 2:
		data_olibKel()
	elif tanlov == 3:
		tanla = int(input("""Tanlang: 
1. Narxni yangilash
2. Modelni yangilash
3. RAM'ni yangilash
Tanglang: """))
		if tanla == 1:
			data_yangilaNarx()
		elif tanla == 2:
			data_yangilaModel()
		elif tanla == 3:
			data_yangilaRAM()
		else:
			print("Iltimos 1-3 oralig'ida son kiriting: ")

	elif tanlov == 4:
		data_ochir1()
	elif tanlov == 5:
		data_ochirHammasini()
	elif tanlov == 0:
		print("Hayr!")



		

