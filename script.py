import subprocess as sp
import pymysql
import pymysql.cursors

def fireAnEmployee():
    """
    Function to fire an employee
    """
    print("Not implemented")

def promoteEmployee():
    """
    Function performs one of three jobs
    1. Increases salary
    2. Makes employee a supervisor
    3. Makes employee a manager
    """
    print("Not implemented")

def deletevideo():
    query1="SELECT ID FROM VIDEOS WHERE REPORTS>=10"
    cur.execute(query1)
    con.commit()
    row=cur.fetchall()
    for tup in row:
        # print(tup["ID"])
    # while row is not None:
    #     # print(row["ID"])
    #     # query2="ALTER TABLE FAVOURITES NOCHECK CONSTRAINT ALL"
    #     # cur.execute(query2)
    #     # con.commit()
        query3="DELETE FROM FAVOURITES WHERE ID=%d"%(tup["ID"])
        cur.execute(query3)
        con.commit()
        query4="DELETE FROM DOWNLOAD WHERE ID=%d"%(tup["ID"])
        cur.execute(query4)
        con.commit()
    query1="DELETE FROM VIDEOS WHERE REPORTS>=10"
    cur.execute(query1)
    con.commit()
        # row=cur.fetchone()
     # query1="ALTER TABLE FAVOURITES WHERE"

def uploadvideo():
    vd={}
    vd["ID"]=int(input("Enter id : "))
    vd["Des"]=input("Enter Description : ")
    vd["AGE"]=int(input("Enter Age restriction : "))
    query = "INSERT INTO VIDEOS (ID,DESCRIPTION,AGE_RESTRICTION) VALUES(%d,'%s',%d)" %(vd["ID"],vd["Des"],vd["AGE"])
    cur.execute(query)
    print(query)
    con.commit()

def forgotpassword(EMAIL_ID):
    phn=input("Enter Phone : ")
    query="SELECT PHONE FROM FORGOT_PASSWORD WHERE EMAIL_ID='%s'"%(EMAIL_ID)
    cur.execute(query)
    con.commit()
    ext=cur.fetchone()
    if(ext["PHONE"]==phn):
        query1="SELECT PASSWORD from ADMIN WHERE PHONE='%s'"%(phn)
        cur.execute(query1)
        con.commit()
        ext=cur.fetchone()
        print("YOUR PASSWORD : ",ext["PASSWORD"])
        print("USE THIS TO LOGIN AGAIN")
        adminaccess(EMAIL_ID)
    else:
        print("NO CREDENTIALS FOUND")

def adminaccess(EMAIL_ID):
    """
    Function prints a report containing 
    the number of hours per week the employee works,
    hourly pay, projects employee works on and so on
    """
    # print("Not implemented")
    pw=input("Enter Password : ")
    query="SELECT PASSWORD from ADMIN WHERE EMAIL_ID='%s'"%(EMAIL_ID)
    cur.execute(query)
    con.commit()
    ext=cur.fetchone()
    # print(ext)
    # print(pw)
    if(ext["PASSWORD"]==pw):
        upl=input("Do you want to upload video (y/n)?")
        if(upl=='y'):
            uploadvideo();
        dlv=input("Do you want to delete video (y/n)?")
        if(dlv=='y'):
            deletevideo();
        # dlv=input()
        # print("QQ")
    else:
        forgotpassword(EMAIL_ID)
        # print("NH")
    # print(ext["PASSWORD"])
def watchvideo(EMAIL_ID):
    des=input("Enter video description : ")
    query2 = "SELECT * FROM VIDEOS WHERE DESCRIPTION='%s'" %(des)
    ans2=cur.execute(query2)
    con.commit()
    if(ans2==1):
        print("WATCHING VIDEO")
        dpp=cur.fetchall()
        for tup in dpp:
            print(tup)
            lk=input("DO U LIKE THE VIDEO (y/n)?")
            if(lk=='y'):
                # print(tup["ID"])
                query6="UPDATE VIDEOS SET LIKES=LIKES + 1 WHERE DESCRIPTION='%s'"%(des)
                cur.execute(query6)
                con.commit()
            rep=input("DO U like to report THE VIDEO (y/n)?")
            if(rep=='y'):
                # print(tup["ID"])
                query7="UPDATE VIDEOS SET REPORTS=REPORTS + 1 WHERE DESCRIPTION='%s'"%(des)
                cur.execute(query7)
                con.commit()
        # print("WW")

def useraccess(EMAIL_ID):
    pw=input("Enter Password : ")
    query="SELECT PASSWORD from REG_USER WHERE EMAIL_ID='%s'"%(EMAIL_ID)
    cur.execute(query)
    con.commit()
    ext=cur.fetchone()
    # print(ext)
    # print(pw)
    if(ext["PASSWORD"]==pw):
        upl=input("Do you want to watch video (y/n)?")
        if(upl=='y'):
            watchvideo(EMAIL_ID);
        dlv=input("Do you want to change password (y/n)?")
        if(dlv=='y'):
            # changepassword();
        # dlv=input()
            print("QQ")
    else:
        forgotpassword(EMAIL_ID)
def newvisit():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new visitor's email: ")
        # name = (input("Name (Fname Minit Lname): ")).split(' ')
        # row["Fname"] = name[0]
        # row["Minit"] = name[1]
        # row["Lname"] = name[2]
        row["EMAIL_ID"] = input("EMAIL_ID: ")
        # row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        # row["Address"] = input("Address: ")
        # row["Sex"] = input("Sex: ")
        # row["Salary"] = float(input("Salary: "))
        # row["Dno"] = int(input("Dno: "))

        """
        In addition to taking input, you are required to handle domain errors as well
        For example: the SSN should be only 9 characters long
        Sex should be only M or F
        If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
        """

        query1 = "INSERT INTO VISITORS(EMAIL_ID) VALUES('%s')" %(row["EMAIL_ID"])
        print(query1)
        cur.execute(query1)
        con.commit()
        query2 = "SELECT * FROM ADMIN WHERE EMAIL_ID='%s'" %(row["EMAIL_ID"])
        ans2=cur.execute(query2)
        con.commit()
        query3 = "SELECT * FROM REG_USER WHERE EMAIL_ID='%s'" %(row["EMAIL_ID"])
        ans3=cur.execute(query3)
        con.commit()
        # print(ans2)
        # print(ans3)
        if(ans2==1):
            # print("ans2")
            adminaccess(row["EMAIL_ID"])
        else:
            if(ans3==1):
                # print("ans3")
                useraccess(row["EMAIL_ID"])
            else:
                # print("As")
                row["Password"]=input("Password : ")
                # name = (input("Name (Fname Minit Lname): ")).split(' ')
                row["Fname"] = input("Fname : ")
                row["Mname"] = input("Mname : ")
                row["Lname"] = input("Lname : ")
                row["Phone"] = input("Phone : ")
                row["Age"] = int(input("Age : "))
                query4 = "INSERT INTO REG_USER (EMAIL_ID,PASSWORD,FNAME,MNAME,LNAME,PHONE,AGE) VALUES ('%s','%s','%s','%s','%s','%s',%d)"%(row["EMAIL_ID"],row["Password"],row["Fname"],row["Mname"],row["Lname"],row["Phone"],row["Age"])
                cur.execute(query4)
                con.commit()
                query6="INSERT INTO FORGOT_PASSWORD (EMAIL_ID,PHONE) VALUES ('%s','%s')"%(row["EMAIL_ID"],row["Phone"])
                cur.execute(query6)
                con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch==1): 
        newvisit()
    # elif(ch==2):
    #     fireAnEmployee()
    # elif(ch==3):
    #     promoteEmployee()
    # elif(ch==4):
    #     employeeStatistics()
    else:
        print("Error: Invalid Option")

# Global
while(1):
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='V_HUB',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")

        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1. New Visitor")
                # print("2. Fire an employee")
                # print("3. Promote an employee")
                # print("4. Employee Statistics")
                print("2. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if ch==2:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")


    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")