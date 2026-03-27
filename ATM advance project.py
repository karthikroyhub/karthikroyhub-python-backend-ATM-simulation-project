    # internal setup
password=1234
balance=30000
tran_hist=[]
attempts=3
    # passwprd verification. max 3 attempts.
while attempts > 0:
  try:
    pin=(int(input("ENTER THE PIN :")))
  except (ValueError,TypeError,KeyError):
    print("enter four numbers only,try again")
    continue
  
  if pin == password:
    print("login successfull")
    break
  else:
    attempts-=1
    print(f"wrong password, remaining attempts are {attempts}")
if attempts == 0:
  print("no more attempts, account block")
  exit()
    # showing atm options to user
while True:
  print("---ATM---")
  print("1-->diposit \n2-->withdraw")
  print("3-->transaction history \n4-->exit")
    # getting user choice
  try:
    choice=(int(input("select the option : ")))
  except TypeError:
    print("enter only number")
    continue
  match choice:
    
    case 1:#logic for depasit amount
      try:
        num1=(float(input("enter depasit amount:")))
      except TypeError:
        print("enter amount in numbers only")
        continue
      if num1>0:
        total = num1 + balance
        tran_hist.append(f"depasit-->${num1}")
        print("successfully diposited")
        print(f"current balance = {total}")
      else:
        print("enter amount morethan zero, try again")
         
    case 2:#logic for withdraw
      try:
        num2=(float(input("ENTER WITHIDRAW AMOUNT:")))
      except TypeError:
        print("enter amount in numbers only")
        continue
      if num2 <= balance:
        total = balance - num2
        tran_hist.append(f"withidral-->{num2}")
        print("withidral successfull")
        print(f"current balance = {total}")
      else:
        print("insufficient balance, try again")
        continue
      
    case 3:#transaction history
      if len(tran_hist)==0:
        print("no transactions yet")
      else:
        print("transaction history:")
        for i in tran_hist:
          print("-->",i)
          
    case 4:#taking exit
      print("thankyou for using ATM")
      print("visit again")
      break
      
        
        
        
      
        
        
        
    
  
  

    
      
    
    
    