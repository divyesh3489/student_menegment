import mysql.connector as my
def branch(e_no):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    e_no=str(e_no)
    q = f"select branch from student where enroll_no='{e_no}'"
    cur.execute(q)
    for i in cur:
        return i[0]
def check_enroll(enroll):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    q = "select * from student join marks on student.enroll_no=marks.enroll_no join attendance on marks.enroll_no=attendance.enroll_no"
    cur.execute(q)
    for i in cur:
        if i[0] == str(enroll):
            return True
    return False


def marks(enroll):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    enroll = str(enroll)
    q = f"select * from student join marks on student.enroll_no=marks.enroll_no where student.enroll_no='{enroll}'"
    cur.execute(q)
    for i in cur:
        if check_enroll(enroll):
            l = [i[0], i[1], i[2], i[3], i[5], i[6], i[7], i[8]]
    return l


def attendance(enroll):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    enroll = str(enroll)
    q = f"select * from student join attendance on student.enroll_no=attendance.enroll_no where student.enroll_no='{enroll}'"
    cur.execute(q)
    for i in cur:
        l = [i[0], i[1], i[2], i[3], i[5], i[6], i[7], i[8]]
    return l


def check_branch(branch):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    q = f" select DISTINCT(Branch) from student"
    cur.execute(q)
    for i in cur:
        if i[0] == branch:
            return True
    return False


def check_roll(roll, branch):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    q = f" select roll_no from student where branch='{branch}'"
    cur.execute(q)
    for i in cur:
        if i[0] == str(roll):
            return False
    return True


def insert_student(e_no, r_no, name, branch):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    e_no=str(e_no)
    r_no=str(r_no)
    q = f"insert into student values ('{e_no}','{r_no}','{name}','{branch}')"
    cur.execute(q)
    connect.commit()


def insert_marks(e_no, fcsp1, fsd1, de, total):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    e_no=str(e_no)
    q = f"insert into marks values ('{e_no}',{fcsp1},{fsd1},{de},{total})"
    cur.execute(q)
    connect.commit()


def insert_attn(e_no, t1, t2, t3, t4):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    e_no=str(e_no)
    q = f"insert into attendance values ('{e_no}',{t1},{t2},{t3},{t4})"
    cur.execute(q)
    connect.commit()
def delete_student(e_no):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    e_no=str(e_no)
    q = f"delete from student where enroll_no='{e_no}'" 
    cur.execute(q)
    connect.commit()
def delete_marks(e_no):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    e_no=str(e_no)
    q = f"delete from marks where enroll_no='{e_no}'" 
    cur.execute(q)
    connect.commit()
def delete_attn(e_no):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    e_no=str(e_no)
    q = f"delete from attendance where enroll_no='{e_no}'" 
    cur.execute(q)
    connect.commit()
def update(e_no,r_no):
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    e_no=str(e_no)
    r_no=str(r_no)
    q = f"update student set roll_no='{r_no}' where enroll_no='{e_no}'"
    cur.execute(q)
    connect.commit()
def showed():
    connect = my.connect(host="localhost", port="3306",
                         user='root', password="*Dvg2004#", database='my_project')
    cur = connect.cursor()
    q=f"select student.enroll_no,roll_no,name,branch,fcsp1,fsd1,e,total,t1,t2,t3,t4 from student join marks on student.enroll_no=marks.enroll_no join attendance on marks.enroll_no=attendance.enroll_no"
    cur.execute(q)
    row=cur.fetchall()
    for i in row :
        print(i)