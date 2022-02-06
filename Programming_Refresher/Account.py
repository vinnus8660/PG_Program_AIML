from Bank import Bank

class Account(Bank):
    
    def __init__(self, IFSC_Code, bankname, branchname, loc, AccountID, CustObject, balance):
        self.AccountID=AccountID
        self.CustObject=CustObject
        self.balance =  balance
        super().__init__(IFSC_Code, bankname, branchname, loc)
        
    def getAccountInfo(self):
        return "Account_ID: " + str(self.AccountID) +"\nCustomer_Name: " + self.CustObject.custname

    def getBalance(self):
        return int(self.balance)
                
        
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successfull! Balance after Deposit is: " + str(self.getBalance()))
        
        
    def withdrawl(self, amount):
        self.balance -= amount
        print("Withdrawl Successfull! Balance after Withdrawl is: " + str(self.getBalance()))
        
        
        