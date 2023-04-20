#import  functions
from authentication import *

#Ender the username and password
#U_name = line 1 (user name) stored in valid.txt
#P_word = line 2 password (pass word) stored valid.txt
U_name = input("Enter your username: ")
P_word = input("Enter your password: ")
# create the file
file_Write= open ("valid.txt", "a")
file_Write.write("sarjoon"+"\n")
file_Write.write("1212"+"\n")
file_Write.close()
#call the valid file to check the username & password
file = "valid.txt"

#check the username & password
if (signin(U_name,P_word,file) == True):
	log_heading=("Successfully Login")
	print("Successfully Login")
	print("-"*len(log_heading))
	print()
	print("ENTER THE STUDENTS DATA")

#function will workd after the user input the correct user name and password, stored in valid.txt

#Open the file
	file = open("students.txt", "a")

#write the data to file
	fun_stop = "Yes" or "No"
	while fun_stop == "Yes":
	#get the inputs from user
		Student_ID = input("Enter the student's ID: ")
		Student_Name = input("Enter the student's name: ")
		Student_Age = input("Enter the student's age: ")
		Student_Location = input("Enter the student's Location: ")
	#devide the data
		studentdata = Student_ID + "\t\t\t\t" + Student_Name + "\t\t\t\t" + Student_Age + "\t\t\t\t" + Student_Location
		fun_stop = input("Do you want to add another student details? (Yes or No): ")

		if (fun_stop == "Yes"):
			print("-----Enter The Next Student's Data-----")
		else:
			print()
			print("Thank You For Entering the data")
	#write function to store the data in student.txt file
		file.write(studentdata+"\n")

else:
	#Warning Message
	print()
	print()
	print("Unauthorized Access!" ,"Please Enter the Correct UserName & Password.")
