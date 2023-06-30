class BankAccount:
    ledger = []

    def __int__(self):
        self.account_no = 0
        self.name = ""
        self.acc_type = ""
        self.amount = 0
        self.balance = 0
        self.trans_type = ""
        self.trans_date = ""

    def GetLedger(self):
        passbook = {}
        passbook['account_no'] = int(input("Enter Account No : "))
        passbook['name'] = input("Enter Account holder Name : ")
        passbook['trans_date'] = ""
        passbook['amount'] = 0
        passbook['balance'] = 0
        passbook['trans_type'] = ""
        BankAccount.ledger.append(passbook)

    def Credit(self, acc_no):
        passbook = {}
        for passbook in  BankAccount.ledger:
            if passbook['account_no'] == acc_no:
                passbook['amount'] = int(input("Enter Amount to credit :"))
                passbook['trans_date'] = input("Enter date of transaction : ")
                passbook['balance'] += passbook['amount']
                passbook['trans_type'] = 'CR'
            else:
                print("-" * 90)
                print(f"Account No {acc_no}  NOT found in Bank Ledger")
                print("-" * 90)

    def Withdraw(self, acc_no):
        passbook = {}
        for passbook in  BankAccount.ledger:
            if passbook['account_no'] == acc_no:
                amt = int(input("Enter Amount to Withdraw :"))
                if passbook['balance'] >= amt:
                    passbook['amount']=amt
                    passbook['trans_date'] = input("Enter date of transaction : ")
                    passbook['balance'] -= passbook['amount']
                    passbook['trans_type'] = 'DB'
                else:
                    print("-" * 90)
                    print(f" Insufficient  Balance in Account No {acc_no} \n Ledger balance is {passbook['balance']} ")
                    print("-" * 90)
            else:
                print("-" * 90)
                print(f"Account No {acc_no}  NOT found in Bank Ledger")
                print("-" * 90)

    def GetBalance(self, acc_no):
        passbook = {}
        for passbook in  BankAccount.ledger:
            if passbook['account_no'] == acc_no:
                print("-" * 90)
                print("Account No\t Name \t\t\t\t Transaction Date\tTransaction Type\t\tAmount\t\tBalance")
                print("-" * 90)
                print("{0:10}\t{1:20}\t{2:16}\t{3:10}\t{4:10}\t{5:10}".format(passbook['account_no'],
                                                                              passbook['name'],
                                                                              passbook['trans_date'],
                                                                              passbook['trans_type'],
                                                                              passbook['amount'],
                                                                              passbook['balance']))
            else:
                print("-" * 90)
                print(f"Account No {acc_no}  NOT found in Bank Ledger")
                print("-" * 90)
    def ShowLdger(self):
        passbook = {}
        print("-" * 90)
        print("Account No\t Name \t\t\t\t Transaction Date\tTransaction Type\tAmount\t\tBalance")
        print("-" * 90)
        for passbook in  BankAccount.ledger:
            print("{0:10}\t{1:20}\t{2:16}\t{3:10}\t{4:10}\t{5:10}".format(passbook['account_no'],
                                                                          passbook['name'],
                                                                          passbook['trans_date'],
                                                                          passbook['trans_type'],
                                                                          passbook['amount'],
                                                                          passbook['balance']))
        print("-" * 90)

class SavingsAccount(BankAccount):

    def Update_Interest(self):
        passbook = {}
        for passbook in  BankAccount.ledger:
            passbook['balance'] += passbook['balance'] * 0.35
        print("Intrest updated")


# Main Program

BankDetail = SavingsAccount()
ch = 0

while ch != 7:
    try:
        print("-" * 40)
        print("Select your Option")
        print("-" * 40)
        print("1.   Legder Entry")
        print("2.   Credit Amount")
        print("3.   Withdraw Amount")
        print("4.   Get Balance")
        print("5.   Update Interest amount")
        print("6.   Show Bank Details")
        print("7.   Quit")
        print("-" * 40)
        ch = int(input("Enter your option : "))
        if ch == 1:
            BankDetail.GetLedger()
        elif ch == 2:
            Acc_no = int(input("Enter Account Number : "))
            BankDetail.Credit(Acc_no)
        elif ch == 3:
            Acc_no = int(input("Enter Account Number : "))
            BankDetail.Withdraw(Acc_no)
        elif ch == 4:
            Acc_no = int(input("Enter Account Number : "))
            BankDetail.GetBalance(Acc_no)
        elif ch == 5:
            BankDetail.Update_Interest()
        elif ch == 6:
            BankDetail.ShowLdger()
        elif ch == 7:
            print("Thank you for Banking with us .....")
    except ValueError:
        print("Invalid Data ...... ")
    finally:
        print("\n")
