# "Basic ATM simulator with password checker 🏦🏧"
saved_password= "Hellow"
balance= 10000
try_limit= 5

while try_limit>0:
    a=input("Enter password: ")
    if(a==saved_password):
        print("You can access👍")

        while True:
            print("Enter your choice:")
            print("1. Balance check")
            print("2. Deposite")
            print("3. Withdraw")
            print("4. Exit")
            b=input("Enter choice (1-4)--> ")
            
            if(b=="1"):
                print("Your current balance",balance)
                print("THANKYOU🙂")
                
            elif(b=="2"):
                print("You want to deposit!")
                amount=float(input("Enter amount= "))
                if(amount<0):
                    print("Not Possible")
                else:
                    balance=balance+ amount
                    print("Your current balance is",balance)
                    print("THANKYOU🙂")
            
            elif(b=="3"):
                print("You want to withdraw!")
                amount=float(input("Enter amount="))
                if(amount <= 0):
                    print("Amount must be positive")
                    continue
                elif(amount > balance):
                    print("Not possible- insufficient balance")
                    continue
                else:
                    balance-=amount
                    print("Your current balance is",balance)
                    print("THANKYOU🙂")
            
            elif(b=="4"):
                print("GOODBYE🤗")
                break

            else:
                print("INVALID CHOICE😑")
                continue

    else:
        try_limit-=1
        print("WRONG PASSWORD😑")
        print("Only {} more attempts left".format(try_limit))
    
if(try_limit==0):
    print("You can not access it anymore😓")
    print("You can try again after 1 hour ⏱️")
