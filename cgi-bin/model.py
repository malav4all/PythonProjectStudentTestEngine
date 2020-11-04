import os
import pymysql
import random
import copy
connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='engine',autocommit=True)

cursor = connection.cursor()

#------------------------------------------------------------------------------------------------------------------
# Student registration class
class User():
    def __init__(self,id,name,password,course,semester,picture):
        self.id = id
        self.name = name
        self.password = password
        self.course = course
        self.semester = semester
        self.picture = picture

    # To String To convert object to printable Format
    def __str__(self):
        return self.id + "," + self.name + "," + self.password + "," + self.course + "," + self.semester + ","
#---------------------------------------------------------------------------------------------------------------

#Teacher Registration Classs
class Teacher():
    def __init__(self,Tname,Tid,Password):
        self.Tname = Tname
        self.Tid = Tid
        self.Password = Password


    def __str__(self):
        return self.Tname + "," + self.Tid + "," + self.Password + ","
#----------------------------------------------------------------------------------------------------------------------
#Students Registration Fuctions
#Student Registration
def register(id,name,password,course,semester,picture):
    if picture.filename:
        fn = os.path.basename(picture.filename)
        img = picture.file.read()
        file = open("upload_profilepic/"+fn,'wb')
        file.write(img)
        file.close()
    else:
        fn = "defaultpic.jpg"
    user = User(id,name,password,course,semester,fn)
    query = "insert into student values (%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(user.id,user.name,user.password,user.course,user.semester,user.picture))
#Students Login Fuction
def login(id,password):
    query = "select * from student where id=%s and password = %s"
    cursor.execute(query,(id,password))
    data = cursor.fetchall()
    if len(data) < 1:
        return  "INVALID Student ID or Password"
    else:
        return data



#Student Id Validation
def studentIdvalidation(id):
    query = "select * from student where id = %s"
    cursor.execute(query,(id))
    num = cursor.rowcount
    if num == 0:
        return "Student ID Valid"
    else:
        return "Student ID Already Exists"

def student_name(name):
    query = "select * from student where name = %s"
    cursor.execute(query,(name))
    data = cursor.fetchall()
    return data


def fetchAllStudents():
    query = "select * from student"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

#--------@@@-------------------@@@@@@@@-----------------------------------------------------------------------

#Teacher Registration Fuctions
#Teacher Registration
def tregister(Tname,Tid,Password):
    teach = Teacher(Tname,Tid,Password)
    query = "insert into teachers values (%s,%s,%s)"
    cursor.execute(query,(teach.Tname,teach.Tid,teach.Password))

def t_login(Tid,Password):
    query = "select * from teachers where Tid=%s and Password=%s"
    cursor.execute(query,(Tid,Password))
    data = cursor.fetchall()


    if len(data) < 1:
        return "Teacher Do Not Exits"
    else:
        return data

#----------------------------------------------------------------------------------------------------------------------
#Add Question In database Function
def insertQuestion(test_id,question,option_1,option_2,option_3,option_4,answere):
    try:
        query = "insert into question values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(int(test_id),question,option_1,option_2,option_3,option_4,answere))
    except pymysql.IntegrityError:
        return "Question already Exists"
#Fetch All The Question Data In Question database
def getQuestions():
    query = "select * from question"
    cursor.execute(query)
    data = cursor.fetchall()
    return data
#Fetch Answere in database to Check Correct Answere
def checkAns(answere,test_id):
    query = "select answere from question where test_id =%s"
    cursor.execute(query,(test_id))
    data = cursor.fetchall()
    return data

#----------------------------------------------------------------------------------------------------------------------
def storeResult(id,name,test_id,marks):
    query = "insert into result(id,name,test_id,marks) values (%s,%s,%s,%s)"
    cursor.execute(query,(id,name,test_id,marks))

def insertTest(Tid,subject,course):
    query = "insert into test (Tid, subject, course) values (%s, %s, %s)"
    cursor.execute(query,(Tid,subject,course))


def getTest(Tid):
    query = "select * from test where Tid=%s"
    cursor.execute(query, Tid)
    data = cursor.fetchall()
    return data

def fetchAllTest():
    query = "select * from test"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def getSubjects(course):
    query = "select subject from test where course = %s"
    cursor.execute(query, course)
    data = cursor.fetchall()
    return data

def getTestInfo(course, subject):
    query = "select * from test where subject = %s and course = %s"
    cursor.execute(query, (subject, course))
    data = cursor.fetchall()
    return data

def getQues(id):
    query = "select * from question where test_id = %s"
    cursor.execute(query, id)
    data = cursor.fetchall()
    return data
    # num = 5
    # data_copy = copy.deepcopy(data)
    # ques = []
    # while len(ques) <= num:
    #     index = random.randrange(len(data_copy))
    #     ques.append(data_copy.pop(index))
    # return ques
def fetchAllResult():
    query = "select * from result"
    cursor.execute(query)
    data = cursor.fetchall()
    return data
