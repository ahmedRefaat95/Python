#!/usr/bin/python -tt

import sys
import os.path

#creating a global list in which the data entries are saved after retrieval
dict_list=[]

#Function to read the contacts from the data base
def getData():

  if os.path.isfile('data.txt'):
    #Opening the file of the data base
    f=open('data.txt','r')
    #reading each line at a time and appending to the list
    for line in f:
      dict_list.append(line)
    #closing the file after data retrieval
    f.close()
  else:
    None
  
  return

def add():

  i=5
  #creating a dictionary to save the data entries
  dict={}
  
  #getting the name of the contact from the user
  name_user = input("Enter the name of the contact : ") 
  #checking if the input string is empty
  if not name_user:
    #creating a while which breaks when the user inputs a non empty string
    while i<6:
      name_user = input("Enter the name of the contact : ")
      if not name_user:
        None
      else:
        break
    dict ['name'] = name_user
  else:
    dict ['name'] = name_user
    
  #getting the email of the contact from the user
  email = input("Enter the email or type NA: ") 
  #checking if the input string is empty
  if not email and email!="NA":
    #creating a while which breaks when the user inputs a non empty string
    while i<6:
      email = input("Enter the email or type NA: ")
      if not email and email!="NA":
        None
      else:
        break
    dict ['email'] = email
  else:
    dict ['email'] = email
  
  #getting the number of the contact from the user
  number = input("Enter the phone number : ") 
  #checking if the input string is empty
  if not number:
  #creating a while which breaks when the user inputs a non empty string
    while i<6:
      number = input("Enter the phone number : ")
      if not number:
        None
      else:
        break
        
    dict ['number'] = number    
  else:
    dict ['number'] = number
  
  #checking if the data base file exists
  if os.path.isfile('data.txt'):
    #opening the file in append mode to add the new contact
    f=open('data.txt','a')
    f.write( str(dict)+"\n" )
    f.close()
  
  else:
    #creating the data base file first
    f=open('data.txt','w')
    f.close()
    #appending the new contact
    f=open('data.txt','a')
    f.write( str(dict)+"\n" )
    f.close()
  
  return

def remove():

  #creating a flag to indicate if the contact is found and removed or not
  found = 0
  
  #checking if the list of dictionaries is not empty
  if len(dict_list)!=0:
  
    #getting the name of the contact which will be deleted from the phone book
    name_user = input("Enter the name of the contact to be deleted : ")
  
    #loop to read each dictionary from the list
    for i in dict_list:
      #evaluating the string from the list to convert it back to dictionary
      dict = eval(i)
      if dict['name']== name_user:
        print("Contact deleted successfully!")
        del dict_list[ dict_list.index(i) ]
        found =1
      else:
        None
        
    if found ==0:
      print("Contact was not found!")
    else:
      None
     
  else:
    print("phone book is empty!")
  
  f=open('data.txt','w')
  
  for newLine in dict_list:
    f.write(newLine)

  f.close()
  return


def viewall():
  
  #checking if the list of dictionaries is not empty
  if len(dict_list)!=0:
    
    #loop to fetch each dictionary from the list
    for i in dict_list:
      #converting the string back to dictionary
      dict = eval(i)
      #printing the data of each contact
      print ('Name: %(name)s , email: %(email)s , phone number: %(number)s '% dict)
  else:
    print("Phone book is empty!")
  return

def main():

    #checking if there are input arguments
    if len(sys.argv)==2:
    
      getData()
      
      if sys.argv[1] == "add":
        add()
      elif sys.argv[1] == "remove":
        remove()
      elif sys.argv[1] == "viewall":
        viewall()
      else:
        print("Invalid command")
        print("please enter one of these command : add - remove - viewall");
    elif len(sys.argv)>2:
      print("please enter one command only : add - remove - viewall")
    else:
      print("please enter a command : add - remove - viewall");
    
      
if __name__ == '__main__':
  main()
  