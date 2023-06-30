import MySQLdb
from MySQLdb import MySQLError
class employee:
    def __init__(self):
        self.conn = MySQLdb.connect(host="localhost",user="root",password="root", database = "EmpDB")
        self.cur = self.conn.cursor()
    def createtbl(self):
        self.cur.execute("drop table IF EXISTS employee")
        sql = "create table employee (empno int PRIMARY KEY, empname varchar(50), empsal int)"
        self.cur.execute(sql)
        print("Employee table created....")
    def insertRec(self):
        print('\n Details of employee-')
        n = int(input("How many employee ? "))
        for i in range(n):
            while True:
                empno = input("\n Enter employee no:")
                if empno.isdigit():
                    empno=int(empno)
                    break
                else:
                    print("Invalid Empoyee Code.....Try again")
                    empname = input("Enter employee name:")
            while True:
                empsal = input("Enter employee salary:")
                if empsal.isdigit():
                    empsal=int(empsal)
                    break
                else:
                    print("Invalid Salary Data ....Try again...")
            try:
                sql = f"insert into employee values({empno},'{empname}',{empsal})"
                self.cur.execute(sql)
                self.conn.commit()
                print("Record inserted successfully")
            except MySQLError as err:
                print(err)
            finally:
                self.conn.commit()
    def displayAll(self):
        try:
            self.cur.execute(f"select * from employee ")
            rows = self.cur.fetchall()
            print("-" * 60)
            print("Emp. No\t\t\tEmployee Name\t\t\t\t\tSalary")
            print("-" * 60)
            for r in rows:
                print(f"{r[0]:8}\t\t{r[1]:25}\t{r[2]:12}")
            print("-"*60)
            print("\nTotal number of rows:", self.cur.rowcount)
        except MySQLError as err:
            print(err)
        finally:
            self.conn.commit()
    def displayRec(self):
        while True:
            eno=input("Enter the employee number to be display : ")
            if eno.isdigit():
                eno = int(eno)
                break
            else:
                print("Invalid Employee Code.....Try again")
        try:
            self.cur.execute(f"select * from employee where empno={eno}")
            rows = self.cur.fetchall()
            print("\nLatest records are")
            print("-" * 60)
            print("Emp. No\t\t\tEmployee Name\t\t\t\t\t\tSalary")
            print("-" * 60)
            for r in rows:
                print(f"{r[0]:8}\t\t{r[1]:25}\t{r[2]:12}")
            print("-"*60)
        except MySQLError as err:
            print(err)
        finally:
            self.conn.commit()
    def displaysal(self):
        while True:
            sal_max = input("\nEnter salary Maximum Limit :")
            if sal_max.isdigit():
                sal_max = int(sal_max)
                break
            else:
                print("Invalid Employee salary.....Try again")
        while True:
            sal_min=input("Enter salary Minimum Limit :")
            if sal_min.isdigit():
                sal_min = int(sal_min)
                break
            else:
                print("Invalid Employee salary....Try again")
        try:
            self.cur.execute(f"select * from employee where empsal between {sal_min} and {sal_max}")
            rows = self.cur.fetchall()
            print("\nLatest records are")
            print("-" * 60)
            print("Emp. No\t\t\tEmployee Name\t\t\t\t\tSalary")
            print("-" * 60)
            for r in rows:
                print(f"{r[0]:8}\t\t{r[1]:25}\t{r[2]:12}")
            print("-" * 60)
            print("\nTotal number of rows:", self.cur.rowcount)
        except MySQLError as err:
            print(err)
        finally:
            self.conn.commit()
    def close_DB(self):
        self.conn.close()
obj = employee()
obj.createtbl()
while True:
     print("\n...... Menu ......")
     print("1. Insert New record into Employee Table")
     print("2. Display All Employees Records")
     print("3. Display Specific Employee record ")
     print("4. Display Employee details of specific Salary range")
     print("5. Exit")
     ch=int(input("\n What is your Choice ...? "))
     if ch == 1:
         obj.insertRec()
     elif ch == 2:
        obj.displayAll()
     elif ch == 3:
        obj.displayRec()
     elif ch == 4:
         obj.displaysal()
     elif ch == 5:
        obj.close_DB()
        print("\n-------- Done --------")
        break
     else:
          print("Invalid Input choice. Try again ....")
