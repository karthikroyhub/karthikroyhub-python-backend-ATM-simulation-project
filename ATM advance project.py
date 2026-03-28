#taking internal setup----------------------------------
password=1234
balance=30000
tran_hist=[]
attempts=3
total=0
#verify password, 3 attempts only.------------------------
while (attempts>0):
  print("             ")
  try:
    pin=int(input("Enter The Password: "))
  except (ValueError,TypeError,KeyError):
    attempts-=1
    print("please Enter Password in Numbers only \n your remaing attempt are: ",attempts)
    continue
  if pin==password:
    print("login successfull, please wait..,")
    break
  else:
    attempts-=1
    print("wrong password, remaining attempts are",attempts)
    continue
if attempts==0:
  print("no more attempts, account blocked")
  exit()
#showing ATM menu to the costomer-------------------------------
while True:
  print("              ")
  print("!----- ATM -----!")
  print("1--->DIPOSIT \n2-->WITHIDRAW \n3-->BALANCE CHECK")
  print("4-->TRANSACTION HISTORY \n5-->EXIT")
  print("           ")
  try:
    choice=int(input("enter the choice:"))
  except (ValueError,TypeError,KeyError):
    print("please choose only number above options")
    continue
  match choice:
    case 1:
      try:
        num1=float(input("Enter the DEPOSIT Amount:"))
      except (ValueError,TypeError,KeyError):
        print("enter amount in numbers only...,")
        continue
      if num1>0:
        total= balance + num1
        tran_hist.append(f"DEPOSIT-->{num1}-->Total amount:{total}")
        print("successfully dipositted")
        print("Current balance:",total)
      else:
        print("for this Amount deposit not possible. try again")
        
    case 2:
      try:
        num2=float(input("Enter the WITHIDRAL Amount:"))
      except (ValueError,TypeError,KeyError):
        print("enter amount in numbers only...,")
        continue
      if balance > num2:
        total = balance - num2
        tran_hist.append(f"WITHIDRAW-->{num2}-->Total amount:{total}")
        print("Amount successfully CREDITED")
        print("Current Balance:",total)
      else:
        print("insufficient balance, try again")
        continue
      
    case 3:
      print("Account balance:",total)
      continue
    
    case 4:
      if len(tran_hist)==0:
        print("no transactions yet")
      else:
        print("TRANSACTION HISTORY")
        for i in tran_hist:
          print("--->",i)
          continue
    
    case 5:
      print("thank you for using ATM, visit again..,")
      print("           ")
      exit()
      
      
    
      
        
        
      
        
  


