mas_pwd = input("Enter the passwerd to edit or viev the file:")
from cryptography.fernet import Fernet

def add():
      name = input("account name: ")
      pwd = input("account password: ")
       
      with open('passwords.txt','a') as f:
            f.write(name + "|" + pwd + "\n")
def view():
      with open('passwords.txt','r') as f:
            for line in f:
                name, pwd = line.strip().split('|')
                print(f"Account: {name}, Password: {pwd}")
while mas_pwd == "1234":
     print("You can edit or view the file now.")
     ask = input("do you want to add or view the file? (add/view) or type q to quit: ").lower()
     if ask == "q":
        break 
     elif ask == "add":
        add()
     elif ask == "view":
        view()
     else:
      print("You entered the wrong command, try again.")
      continue
        
else:
    print("You entered the wrong password, try again.")
    quit()