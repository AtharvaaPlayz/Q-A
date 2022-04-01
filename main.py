Username = input("please enter username")
Password = input("Password")  
print(Username)
print("hi") 
print(Username)
print("welcome to this app")
Question1 = input("what is 9x9")
if(Question1 == ' 81'):
               print("Loading")
else:
  print("bye kid")
  quit()

if(Password == Username):
  print("The username and the password shoudn't be the same")
  quit()
else:
  print("loading completed")
  print("Welcome to Q|A's")

Subject = input("Choose one subject : Math Science C.S SSc Astronomy")
if(Subject == ' Math'):
      Q1M = input("what is 10 divided [49-10] + [45x2]")
      if(Q1M == ' 12.9'):
         print("correct answer")
      else:
       print("wrong answer try again")
       quit()