import mydatabase as db
import matplotlib.pyplot as plt
import time

class Student:
    def colors(self):
        self.color2=[]
        for i in self.marks:
            if i<35:
                self.color2.append("red")
            else:
                self.color2.append("blue")
        return self.color2
    def s_menu(self):
        n = int(input("1.For Show Marks\n2.For Show Attendance\n"))
        if n == 1:
            self.show_marks()
        elif n == 2:
            self.attn()
        else:
            self.s_menu()
    def show_marks(self):
        self.enroll_no = int(input("Enter Your Enroll_no"))
        lable=["FCSP-1","FSD1","DE","TOTAL"]
        if db.check_enroll(self.enroll_no):
            self.l = db.marks(self.enroll_no)
            self.marks=self.l[4:]
            plt.title(
                f"Enroll_no:{self.l[0]}    Roll_no:{self.l[1]}    Name:{self.l[2]}   Branch:{self.l[3]}")
            plt.bar(lable, self.marks,color=self.colors())
            plt.ylabel("Marks")
            plt.xlabel("Subject")
            plt.show()
        else:
            print("Recoder not Found")

    def attn(self):
        self.enroll_no = int(input("Enter Your Enroll_no"))
        if db.check_enroll(self.enroll_no):
            test = ["test1", "test2", "test3", "test4"]
            a = db.attendance(self.enroll_no)
            self.week = a[4:]
            plt.title(
                f"Enroll_no:{a[0]}    Roll_no:{a[1]}    Name:{a[2]}   Branch:{a[3]}")
            plt.bar(test, self.week, color=self.color())
            plt.ylabel("Attendance In Percentage")
            plt.show()
        else:
            print("Please Enter Valid Enroll_no")

    def color(self):
        self.color1 = []
        for i in self.week:
            if i < 75.0:
                self.color1.append("red")
            elif i >= 75 and i < 80:
                self.color1.append("orange")
            else:
                self.color1.append("blue")
        return self.color1


class Teacher:
    def T_menu(self):
        n = int(
            input("1.For Insert New Student Data\n2.For Update\n3.remove Student\n4.show_data\n"))
        if n == 1:
            self.insert()
        elif n == 2:
            self.update()
        elif n == 3:
            self.delete()
        elif n == 4:
            self.show_data()
        else:
            self.T_menu()

    def insert_mark(self):
        while True:
            self.__fcsp1 = float(input("Enter Marks Of fcsp1:"))
            if self.__fcsp1 < 0 or self.__fcsp1 > 100:
                print("Mark Cannot Be Negative or Mark Cannot be grater then 100")
            else:
                break
        while True:
            self.__fsd1 = float(input("Enter Marks Of fsd1:"))
            if self.__fsd1 < 0 or self.__fsd1 > 100:
                print("Mark Cannot Be Negative or Mark Cannot be grater then 100")
            else:
                break
        while True:
            self.__de = float(input("Enter marks Of DE:"))
            if self.__de < 0 or self.__de > 100:
                print("Mark Cannot Be Negative or Mark Cannot be grater then 100")
            else:
                break
        self.__total = self.__fcsp1+self.__fsd1+self.__de

    def insert_atten(self):
        while 1:
            self.__t1_total = int(input("Enter Total Number of Lecture T1:"))
            self.__t1_attn = int(
                input("Enter Number Of Lecture Attended In T1:"))
            if self.__t1_total < self.__t1_attn or self.__t1_total < 0 or self.__t1_attn < 0:
                print("Totlal Number Of Lecture Is Grater Then Attended Lecture")
                print("                   OR                                   ")
                print("Total Number Of Lecture Cannot Less Then 0")
                print("                   OR                                   ")
                print("Number Of Attended Lecture Cannot Less Then 0")
            else:
                break
        self.__t1 = round((self.__t1_attn/self.__t1_total)*100, 2)
        while 1:
            self.__t2_total = int(input("Enter Total Number of Lecture T2:"))
            self.__t2_attn = int(
                input("Enter Number Of Lecture Attended In T2:"))
            if self.__t2_total < self.__t2_attn or self.__t2_total < 0 or self.__t2_attn < 0:
                print("Totlal Number Of Lecture Is Grater Then Attended Lecture")
                print("                   OR                                   ")
                print("Total Number Of Lecture Cannot Less Then 0")
                print("                   OR                                   ")
                print("Number Of Attended Lecture Cannot Less Then 0")
            else:
                break
        self.__t2 = round((self.__t2_attn/self.__t2_total)*100, 2)
        while 1:
            self.__t3_total = int(input("Enter Total Number of Lecture T3:"))
            self.__t3_attn = int(
                input("Enter Number Of Lecture Attended In T3:"))
            if self.__t3_total < self.__t3_attn or self.__t3_total < 0 or self.__t3_attn < 0:
                print("Totlal Number Of Lecture Is Grater Then Attended Lecture")
                print("                   OR                                   ")
                print("Total Number Of Lecture Cannot Less Then 0")
                print("                   OR                                   ")
                print("Number Of Attended Lecture Cannot Less Then 0")
            else:
                break
        self.__t3 = round((self.__t3_attn/self.__t3_total)*100, 2)
        while 1:
            self.__t4_total = int(input("Enter Total Number of Lecture T4:"))
            self.__t4_attn = int(
                input("Enter Number Of Lecture Attended In T4:"))
            if self.__t4_total < self.__t4_attn or self.__t4_total < 0 or self.__t4_attn < 0:
                print("Totlal Number Of Lecture Is Grater Then Attended Lecture")
                print("                   OR                                   ")
                print("Total Number Of Lecture Cannot Less Then 0")
                print("                   OR                                   ")
                print("Number Of Attended Lecture Cannot Less Then 0")
            else:
                break
        self.__t4 = round((self.__t4_attn/self.__t4_total)*100, 2)

    def insert(self):
        self.__newenroll_no = int(input("Enter New Enroll Number:"))
        if not db.check_enroll(self.__newenroll_no):
            self.__roll_no = int(input("Enter Roll Number:"))
            self.__branch = input("Enter Branch:")
            if db.check_branch(self.__branch):
                if db.check_roll(self.__roll_no, self.__branch):
                    print("1")
                    self.__name = input("Enter Name:")
                    self.insert_mark()
                    self.insert_atten()
                    db.insert_student(
                        self.__newenroll_no, self.__roll_no, self.__name, self.__branch)
                    db.insert_marks(self.__newenroll_no, self.__fcsp1,
                                    self.__fsd1, self.__de, self.__total)
                    db.insert_attn(self.__newenroll_no, self.__t1,
                                   self.__t2, self.__t3, self.__t4)

                else:
                    print("Roll Number Is Already Exist In This Branch")
                    self.insert()
            else:
                self.__name = input("Enter Name:")
                self.insert_mark()
                self.insert_atten()
                db.insert_student(self.__newenroll_no,
                                  self.__roll_no, self.__name, self.__branch)
                db.insert_marks(self.__newenroll_no, self.__fcsp1,
                                self.__fsd1, self.__de, self.__total)
                db.insert_attn(self.__newenroll_no, self.__t1,
                               self.__t2, self.__t3, self.__t4)

        else:
            print("Enter Roll Number Is Exist")

    def update(self):
        self.__enroll_no = int(input("Enter Enroll Number Of Student:"))
        if db.check_enroll(self.__enroll_no):
            self.__newroll_no = int(input("Enete New Roll Number:"))
            b = db.branch(self.__enroll_no)
            if db.check_roll(self.__newroll_no, b):
                db.update(self.__enroll_no, self.__newroll_no)
                print("Record Updated Successful")
            else:
                print("Roll Number Is Already Exist In This Branch")
        else:
            print("Record Not Found")

    def delete(self):
        self.__newenroll_no = int(
            input("Enter Enroll Number Of Student You want To delet:"))
        if db.check_enroll(self.__newenroll_no):
            db.delete_student(self.__newenroll_no)
            db.delete_marks(self.__newenroll_no)
            db.delete_attn(self.__newenroll_no)
            print("Record Deleted Successful")
        else:
            print("Record Not Found")

    def show_data(self):
        print("(enroll_no,roll_no,name,branch,fcsp1 marks,fsd1 marks,de marks,total,t1,t2,t3,t4)")
        db.showed()


class Main_menu(Teacher, Student):
    user = 'Divyesh'
    Password = "*Dvg2004#"

    def main(self):
        n = int(input("1.For Teacher\n2.For Student\n3.Exit\n"))
        if n == 1:
        
            username = input("Enter user name:")
            pas = input("Enter password:")
            if Main_menu.user == username and Main_menu.Password == pas:
                self.T_menu()
                self.main()
            else:
                print("Invalid password Or Invalid Username")
                self.main()
        elif n == 2:
            self.s_menu()
            self.main()
        elif n==3:
            pass
        else:
            self.main()


obj = Main_menu()
obj.main()
