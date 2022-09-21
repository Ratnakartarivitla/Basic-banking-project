#creating users dict()
users = {'code':"code@123",'test':"test@123"}

# inputs username and password
userName = input("Enter your user name : ")


#checking if user exists in the data source
if userName in users.keys():
  password = input("Enter your password : ")
#checking the user authentication
  if users[userName] == password:
    print(''' choose 1 for ministatement
        2 for credit
        3 for debit
        4 for user details ''')
    operation = int(input("Enter the operation to be performed : "))
    if operation == 1:
      print("This is your mini statement")
    elif operation == 2:
      print("These are your credit details")
    elif operation == 3:
      print("These are your debit details")
    elif operation == 4:
      print('Hi',userName,"you are viewing your profile")
    else:
      print('you choose the wrong option..... good bye')
  else:
    print('invalid username or password')
else:
  print('no user found.... Thank you....')
