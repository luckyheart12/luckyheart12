#Authentication File
#Define the Authentication file
def signin(username,password,filename):

# read the file
	file = open(filename,"r")
	U_Name = file.readline().strip()
	P_word = file.readline().strip()
	file.close()

#Match the username & password
	if (username == U_Name and password == P_word):
		return True
	else:
		return False