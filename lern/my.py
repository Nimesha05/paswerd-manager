from cryptography.fernet import Fernet


def load_key():
     file = open("key.key", "rb")
     key = file.read()
     file.close()
     return key

mas_pwd = input("Enter the passwerd to edit or viev the file:")
key = load_key() + mas_pwd.encode()
fer = Fernet(key)

# '''
# def generate_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#          key_file.write(key)
# '''

# generate_key()




def add():
    name = input("account name: ")
    pwd = input("account password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



def view():
      with open('passwords.txt','r') as f:
            for line in f.readlines():
                deta = line.rstrip()
                name, pwd = deta.split("|")
                print("User", name, "| has password", fer.decrypt(pwd.encode()).decode())
                
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