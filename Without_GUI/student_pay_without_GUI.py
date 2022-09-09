import sys
new_dict = {} # Global dictionary [Any function can access it]

def file_to_dict():
  f = open("student_info.txt")
  for line in f: 
    (key, val1, val2, val3, val4, val5) = line.split() # Splitting each line of the file
    new_dict[int(key)] = [val1, val2, val3, val4, val5] # Adding values to dictionary
  print(new_dict)

def take_input():
  email = input("Enter your email address: ")
  password = input("Enter your password: ")

  return email, password

def authenticate(email, password):
  c = 0
  for key, value in new_dict.items():
    if(value[2] == email and value[3] == password): # Matching email and password 
      id = key
      print(" ** YOU ARE LOGGED IN SUCCESSFULLY **")
      c = 1
      break
  if(c == 0):
    print(" ** INVALID E-MAIL OR PASSWORD **")
    sys.exit()
    

  return id

def details(new_dict, id):
  for key, value in new_dict.items():
    if(key == id):
      fName = value[0]
      lName = value[1]
      email = value[2]
      password = value[3]
      due_amount = value[4]

  print("\n ## YOUR DETAILS: ")
  print("   --> ID: ", id)
  print("   --> First Name: ", fName)
  print("   --> Last Name: ", lName)
  print("   --> E-mail: ", email)
  print("   --> Password: ", password)
  print("   --> Tution fee (Due): ", due_amount)

def payment(id):
  amount = int(input("Enter the amount you want to pay: "))
  for key, value in new_dict.items():
    if(key == id):
      new_amount = int(value[4]) - amount
      updated_dict = {key:[value[0], value[1], value[2], value[3], new_amount]} # Updating dictionary
      new_dict.update(updated_dict)
      print(" \n** Paid Successfully **")
      break

def menu(id):
  print("\n(1) DETAILS")
  print("(2) PAYMENT")
  print("(3) Exit")
  choice = int(input("Select option: "))

  if(choice == 1):
    details(new_dict, id)
  elif(choice == 2):
    payment(id)
  elif(choice == 3):
    print("Thank you for visitng")
    sys.exit()
  else:
    print("Invalid input. Please try again")
    menu()


if __name__ == "__main__":


	file_to_dict()
	email, password = take_input()

	id = authenticate(email, password)

	while(1): # infinity loop
	  menu(id)