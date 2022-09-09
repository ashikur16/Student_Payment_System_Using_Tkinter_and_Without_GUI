from ctypes import alignment
from logging.config import IDENTIFIER
import sys
from turtle import position
new_dict = {} # Global dictionary


def file_to_dict():
  f = open("student_info.txt")
  for line in f: 
    (key, val1, val2, val3, val4, val5) = line.split() # Splitting each line of the file
    new_dict[int(key)] = [val1, val2, val3, val4, val5] # Adding valules to dictionary


def authenticate(email, password):
  c = 0
  for key, value in new_dict.items():
    if(value[2] == email and value[3] == password): # Matching email and password 
      id = key
      print(" ** YOU ARE LOGGED IN SUCCESSFULLY **")
      Label (window, text="** YOU ARE LOGGED IN SUCCESSFULLY **", bg="black", fg="green", font="none 12 bold") .grid(row=3, column=1, sticky=W)
      c = 1
      break
  if(c == 0):
    print(" ** INVALID E-MAIL OR PASSWORD **")
    Label (window, text="** INVALID E-MAIL OR PASSWORD **", bg="black", fg="red", font="none 12 bold") .grid(row=3, column=1, sticky=W)
    #sys.exit()
    
  return id

def details(new_dict, id):
  for key, value in new_dict.items():
    if(key == id):
      fName = value[0]
      lName = value[1]
      email = value[2]
      password = value[3]
      due_amount = value[4]

  output.insert('1.0', 'ID: ')
  output.insert('2.0',id)
  output.insert('3.0', '\nFirst Name: ')
  output.insert('4.0',fName)
  output.insert('5.0', '\nLast Name: ')
  output.insert('6.0',lName)
  output.insert('7.0', '\nE-mail: ')
  output.insert('8.0',email)
  output.insert('9.0', '\nPassword: ')
  output.insert('10.0',password)
  output.insert('11.0', '\nTution fee (Due): ')
  output.insert('12.0',due_amount)
  

def payment(id, amount):

  for key, value in new_dict.items():
    if(key == id):
      new_amount = int(value[4]) - amount
      updated_dict = {key:[value[0], value[1], value[2], value[3], new_amount]} # Updating dictionary
      new_dict.update(updated_dict)
      print(" \n** Paid Successfully **")
      output.delete(0.0, END)
      details(new_dict, id)
      break


def click():
  global global_id
  email = emailField.get()
  password = passwordField.get()
  print(email)
  print(password)
  id = authenticate(email, password)

  Button(window, text="Log out", width=6, command=Logout_Click).grid(row=8, column=5, sticky=W)

  output.delete(0.0, END)
 
  details(new_dict, id)

  amount = paymentField.get()
  print(amount)
  amount = int(str(amount))
  payment(id, amount)

  Label (window, text="** Paid Successfully. Please see your details **", bg="black", fg="green", font="none 12 bold") .grid(row=33, column=0, sticky=W)

def Logout_Click():
  window.destroy()

d = {} # Empty dictionary
file_to_dict()
 

from tkinter import *
from tkinter import font
window=Tk()
window.title('Student Log In System')
window.configure(background="black")
window.geometry("900x400")


Label(window,text="Student Log In System",bg="black", fg="Yellow", font="none 40 bold", anchor=CENTER) .grid(row=2, column=1, sticky=W)


Label (window, text="Enter your E-mail Address: ", bg="black", fg="white", font="none 20 bold") .grid(row=8, column=0, sticky=W)
emailField = Entry(window, width=30, bg="white")
emailField.grid(row=8, column=1, sticky=W)


Label (window, text="Enter your password: ", bg="black", fg="white", font="none 20 bold") .grid(row=10, column=0, sticky=W)
passwordField = Entry(window, width=30, bg="white")
passwordField.grid(row=10, column=1, sticky=W)


Button(window, text="Log in", width=6, command=click).grid(row=12, column=0, sticky=W)

Label (window, text="Your Details: ", bg="black", fg="green", font="none 20 bold") .grid(row=16, column=0, sticky=W)
output = Text(window, width=77, height=8, wrap = WORD, background="white")
output.grid(row=18, column=0, columnspan=2, sticky=W)


Label (window, text="Enter the amount you want to pay: ", bg="black", fg="white", font="none 20 bold") .grid(row=22, column=0, sticky=W)
paymentField = Entry(window, width=30, bg="white")
paymentField.grid(row=22, column=1, sticky=W)
Button(window, text="Confirm Payment", width=10, command=click).grid(row=26, column=0, sticky=W)


window.mainloop() # to stable the window