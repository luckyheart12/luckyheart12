#import  functions
from authentication import *

#Ender the username and password
#U_name = line 1 (user name) stored in valid.txt
#P_word = line 2 password (pass word) stored valid.txt
U_name = input("Enter your username: ")
P_word = input("Enter your password: ")
file = ("valid.txt")
print()
#check the username & password
if (signin(U_name,P_word,file) == True):
	log_heading=("**** Successfully Login ****")
	width = 70
	center = log_heading.center(width)
	print(center)

	file = open("students.txt", "r")
	#Print the headign
	#here i used ("\033[1m'-headign- \033[0m") to bold the headign
	studentdata = ("\033[1mStudent ID\t\tStudent Name\t\tStudent Age\t\tStudent Location\033[0m")
	print()
	Mainheading = ("\033[1m********STUDENTD DETA********\033[0m")
	width = 75
	center = Mainheading.center(width)
	print(center)
	print()
	print(studentdata)
	#print the underline

	sid="Student ID"
	print("-" * len(sid),end='')

	sn="Student Name"
	print("     ","-" * len(sn),end='')

	sa="Student Age"
	print("       ", "-" * len(sa),end='')

	sl="Student Location"
	print("    ", "-" * len(sl))
	print()



	#arrays to store the datas

	S_Id = []
	S_name = []
	S_age = []
	S_location = []

	#append the data into created arrays

	for value in file:
		details = value.strip().split("\t\t\t\t")
		S_Id.append(details[0])
		S_name.append(str(details[1]))
		S_age.append(int(details[2]))
		S_location.append(details[3])

	#print the data
	
		print(value.strip())
	print()
	print("No. of Students: ",len(S_Id))
	print("Lowest Age of Student: ",min(S_age))
	print("Highest Age of Student: ",max(S_age))

else:
	#Warning Message
	print()
	print("Unauthorized Access!" ,"Please Enter the Correct User Name & Password.")


