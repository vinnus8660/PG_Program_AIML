from Account import Account

class SavingsAccount(Account):
    
    def __init__(self,IFSC_Code,bankname,branchname,loc,AccountID,CustObject,balance,SMinBalance):
        self.SMinBalance = SMinBalance
        super().__init__(IFSC_Code, bankname, branchname, loc, AccountID, CustObject, balance)
        
    def withdrawl(self, amount):
        if((self.balance - amount) > self.SMinBalance):
            Account.withdrawl(self, amount)
        elif(amount > self.balance):
            print("Sorry...You do not have sufficient balance for this transaction")
        else:
            print("Sorry...We can't allow this transaction, as minimum balance needs to be maintained in your account")

                
            
    def getSavingAccountInfo(self):
        return "Account_ID: " + str(self.AccountID) +"\nCustomer_Name:" + self.CustObject.custname
                
    