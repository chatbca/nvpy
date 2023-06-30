import MySQLdb
from MySQLdb import MySQLError

class Student:
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host='localhost',user='root', password='root', database='studentdb')
            self.cur = self.conn.cursor()
            print("Database Connection successful...")
        except AttributeError as err:
            print(err)
            print("Database Connection Error...")
        finally:
         print("Database Connection process completed ...")

    def createtbl(self):
        try:
            self.cur.execute("drop table marks")
        except AttributeError as err:
            print(err)
        finally:
            sql = "create table marks (reg int PRIMARY KEY, stName varchar(50), m1 int, m2 int, m3 int)"
            self.cur.execute(sql)
            print("Student table created....")

    def valid_marks(self, marks):
        if marks.isdigit():
            if int(marks)>0 and int(marks)<=100:
                return True
            else:
                return False

    def valid_reg(self, reg_no):
        if reg_no.isdigit():
            return True
        else:
            return False

    def insertRec(self):
        print('Enter details of student-')
        try:
            while True:
                reg=input("\nEnter Registration number : ")
                if self.valid_reg(reg):
                    reg = int(reg)
                    break
                else:
                    print("Invalid Data try again....")
            stName = input("Enter student name:")
            while True:
                m1 = input("Enter marks in Python programming : ")
                if self.valid_marks(m1):
                    m1=int(m1)
                    break
                else:
                    print("Invalid data try again....")

            while True:
                m2 = input("Enter marks in Operating System : ")
                if self.valid_marks(m2):
                    m2 = int(m2)
                    break
                else:
                     print("Invalid data try again...")

            while True:
                m3 = input("Enter marks in Multimedia & CGI : ")
                if self.valid_marks(m3):
                    m3=int(m3)
                    break
                else:
                    print("Invalid data try again...")
            sql = f"insert into marks values({reg},'{stName}',{m1},{m2},{m3})"
            self.cur.execute(sql)
            print("Record inserted successfully")
        except AttributeError as err:
            print("Error : ", err)
        finally:
            self.conn.commit()

 # To remove the record from student table
    def displayRec(self):
        try:
            self.cur.execute("select * from marks")
            rows = self.cur.fetchall()
            print("\nLatest record are-")
            print("Reg. No\t\tName of the Student \tM1\tM2\tM3")
            for r in rows:






import MySQLdb
from MySQLdb import MySQLError

class Student:
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host='localhost',user='root', password='root', database='studentdb')
            self.cur = self.conn.cursor()
            print("Database Connection successful...")
        except AttributeError as err:
            print(err)
            print("Database Connection Error...")
        finally:
         print("Database Connection process completed ...")

    def createtbl(self):
        try:
            self.cur.execute("drop table marks")
        except AttributeError as err:
            print(err)
        finally:
            sql = "create table marks (reg int PRIMARY KEY, stName varchar(50), m1 int, m2 int, m3 int)"
            self.cur.execute(sql)
            print("Student table created....")

    def valid_marks(self, marks):
        if marks.isdigit():
            if int(marks)>0 and int(marks)<=100:
                return True
            else:
                return False



    def valid_reg(self, reg_no):
        if reg_no.isdigit():
            return True
        else:
            return False

    def insertRec(self):
        print('Enter details of student-')
        try:
            while True:
                reg=input("\nEnter Registration number : ")
                if self.valid_reg(reg):
                    reg = int(reg)
                    break
                else:
                    print("Invalid Data try again....")
            stName = input("Enter student name:")
            while True:
                m1 = input("Enter marks in Python programming : ")
                if self.valid_marks(m1):
                    m1=int(m1)
                    break
                else:
                    print("Invalid data try again....")

            while True:
                m2 = input("Enter marks in Operating System : ")
                if self.valid_marks(m2):
                    m2 = int(m2)
                    break
                else:
                     print("Invalid data try again...")

            while True:
                m3 = input("Enter marks in Multimedia & CGI : ")
                if self.valid_marks(m3):
                    m3=int(m3)
                    break
                else:
                    print("Invalid data try again...")
            sql = f"insert into marks values({reg},'{stName}',{m1},{m2},{m3})"
            self.cur.execute(sql)
            print("Record inserted successfully")
        except AttributeError as err:
            print("Error : ", err)
        finally:
            self.conn.commit()

 # To remove the record from student table
    def displayRec(self):
        try:
            self.cur.execute("select * from marks")
            rows = self.cur.fetchall()
            print("\nLatest record are-")
            print("Reg. No\t\tName of the Student \tM1\tM2\tM3")
            for r in rows:
                print(f"{r[0]:7}\t{r[1]:20}\t{r[2]:3}\t{r[3]:3}\t{r[4]:3}")

        except ValueError as err:
            print(err)
        finally:
            self.conn.commit()
            print("\nTotal number of records : ", self.cur.rowcount)

    def removeRec(self):
        while True:
            reg = input("\n Enter Reg.no to remove : ")
            if self.valid_reg(reg):
                reg = int(reg)
                break
            else:
                print("Invalid Data try again....")
        sql = f"delete from marks where reg = {reg}"
        try:
            self.st = self.cur.execute(sql)
            if (self.st) == 0:
                print("\nRecord not found")
            else:
                print("\nRecord deleted successfully")
            self.displayRec()
        except ValueError as err:
           print(err)
        finally:
           self.conn.commit()

    def close_DB(self):
        self.conn.close()


# Main Program
obj = Student()
obj.createtbl()
ch = ''
while (ch.upper() != 'N'):
    print('*' * 30)
    print("------ Main Menu ------")
    print('*' * 30)
    print("1. Insert Student Records.")
    print("2. Display Student Records. ")
    print("3. Remove Student Record. ")
    print('*' * 30)
    try:
        op = int(input("Enter your choice : "))
        if op == 1:
            obj.insertRec()
        elif op == 2:
            obj.displayRec()
        elif op == 3:
            obj.removeRec()
        else:
            print("\n Invalid option ....")
    except ValueError as err:
        print("Error in input : ", err)
    finally:
        ch = input("\nDo you want to continue ...(y/n) ?")
print(".... Goodbye ....")
obj.close_DB()
