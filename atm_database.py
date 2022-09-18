import random
import mysql.connector
mydb=mysql.connector.connect(
    
    host="localhost",
    user="root",
    password="Felix@2001",
    database="felixdb"
)
mycursor=mydb.cursor()



class ATM():
    
    def __init__(self,name='',account_number='',amount=0,balance=2000):
        print()
        print("*********welcome to bank of baroda*********")
        print()
        self.name=name
        self.account_number=account_number
        self.balance=balance
        self.amount=amount
        
    def account_detail(self):
        while(1):
            print("#########ACCOUNT DETAILES#########")
            self.name=input("Account holder:").strip().lower()
            self.account_number=input("account number:").strip()
            print("available balance:Rs.",self.baalance)
            print()
        
            x="insert into account_details(name,account_number)valus(%s,%s)"
            y=[self.name,self.account_number]
            mycursor.execute(x.y)
            mydb.commit()
            break        
    def withdraw_cash(self):
        while(1):
            
            self.amount=int(input("enter your withdraw amount:Rs."))
            
            
            if self.amount>self.balance:
                
                print("amount invaild")
                print(f"your savings balance is Rs.{self.balance}")
                print("try again.....")
                print()
                
                
            else:
                
                self.balance=self.balance=self.balance
                print(f"Rs.{self.amount}withdraw  to your account")
                print("your balance is Rs.",self.balance)
                print()
                
                
            x="insert into account_details(AVAILABLE_BALANCE)values(%s)"
            y=[self.balance]
            mycursor.execute(x,y)
            mydb.commit()
            
            
            break
        
    def check_balance(self):
        
        while(1):
            
            print("Available balance:Rs.",self.balance)
            print()
                
            x="insert into account_details(AVILABLE BALANCE)values(%s)"
            y=[self.balance] 
            mycurcor.execute(x,y)
            mydb.commit()
                
            break
    def print_recipt(self):
        while(1):
            
                    
            print("**********bank of baroda*********")
            print()
            print("transaction number: ",{random.randint(10000,1000000)})
            print()
            print(f"account holder: {self.name}")
            print()
            print(f"Account number:{self.account_number}")
            print()
            print("avalible balance: Rs.",self.balance)
            print()
                    
            break
    def main():
        
        f=ATM()
        
        while(1):
            print("**********TRANSACTIONS**********")
            print("1.account details")
            print("2.deposite")
            print("3.withdraw")
            print("4.check balance")
            print("5.print recipt")
            print("6.exit")
            print()
            
            b=int(input("enter your choice->"))
            
            
            
            if b==1:
                f.account_details()
            
            
            elif b==2:
                f.deposit_cash()
                
                
            elif b==3:
                f.withdrew_cash()
                
            elif b==4:
                f.check_balance()
                
            elif b==5:
                f.print_recipt()
                
            elif b==6:
                quit()
                
    def verfiy():
        pin=1430
        
        password=int(input("enter your pin:"))
        
        
        if pin==password:
            print("your pin is correct")
            main()
            
        else:
            print("error! incurrent pin")
            
            
            print("******* thankyou for your transation*********")
            
verify()            
            
                              
                    
                    
                
                        
                
            
            
        
        
                    
        
                    
           