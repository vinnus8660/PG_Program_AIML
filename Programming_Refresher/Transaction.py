from Customer import Customer
from SavingsAccount import SavingsAccount
import re

class Transaction(Customer, SavingsAccount):
    
    customerID = "123456789"
    custname="Vinay"
    address="Hyderabad"
    contactdetails="9866612345"
    IFSC_Code = "YSB008"
    bankname = "YesBank"
    branchname = "Hyderabad"
    loc = "0123456789"
    balance = 50000
    minBalance = 500
    

customer = Customer(Transaction.customerID, Transaction.custname, Transaction.address, Transaction.contactdetails)

accountNo = str(input("Please enter 16 digit Account Number: "))

if re.match("^[0-9]{16}$", accountNo):  
    
    savingsObj = SavingsAccount(Transaction.IFSC_Code,Transaction.bankname,Transaction.branchname,Transaction.loc,accountNo,customer,Transaction.balance,Transaction.minBalance)
    
    print("Please check your details below and Input further details if the info is proper")

    print(savingsObj.getSavingAccountInfo())
    
    print("Your Current Balance is: " + str(savingsObj.getBalance()))
    
    userInput1 = input("Please enter D for Deposit/ W for Withdrwal: ")
    
    if re.match("^[D, d, w, W]{1}$", userInput1):
    
        amount = int(input("Enter Amount: "))
        
        if re.match("^[0-9]+$", accountNo):
        
            if userInput1.casefold()=="d":
                savingsObj.deposit(amount)
                
            elif userInput1.casefold()=="w":
                savingsObj.withdrawl(amount)  
        
            print("Thanks for Banking with us!!! See you again")
            
        else:
            print("Sorry...Wrong Amount Entered...Please try again.")
    else:
        print("Sorry...Wrong Option Selected...Please try again.") 
else:
    print("Sorry...Account Number should be 16 digits only...Please try again.")
    






