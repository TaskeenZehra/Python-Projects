import mysql.connector as ms

def Insert(user,passw):

    conn = ms.connect(host='localhost', user='root', password='yam110stz', database='login_information')
    conn.connect()
    cur = conn.cursor()
    DT=ReadId()
    i=DT[0][0]
    i+=1
    cur.execute(f"insert into login_info(Id,Username,Password) values({i},2'{user}','{passw}')")
    conn.commit()
    conn.close()

def ReadId():
    conn = ms.connect(host='localhost', user='root', password='yam110stz', database='login_information')
    conn.connect()
    cur = conn.cursor()
    cur.execute(f"select Max(Id) from login_info")
    return(cur.fetchall())


def Delete(user,passw):
    conn = ms.connect(host='localhost', user='root', password='yam110stz', database='login_information')
    conn.connect()
    cur = conn.cursor()
    cur.execute(f"delete from login_info where Username='{user}' and Password='{passw}'")
    conn.commit()
    conn.close()

def Update(n,user,passw,new):
    conn = ms.connect(host='localhost', user='root', password='yam110stz', database='login_information')
    conn.connect()
    cur = conn.cursor()
    cur.execute(f"update login_info set {n} ='{new}' where Username = '{user}' and Password = '{passw}'")
    conn.commit()
    conn.close()

def SearchN(user):
    conn = ms.connect(host='localhost', user='root', password='yam110stz', database='login_information')
    conn.connect()
    cur = conn.cursor()
    cur.execute(f"Select * from login_info where Username = '{user}'")
    data=cur.fetchall()
    conn.close()
    print(data)

def SearchP(passw):
    conn = ms.connect(host='localhost', user='root', password='yam110stz', database='login_information')
    conn.connect()
    cur = conn.cursor()
    cur.execute(f"Select * from login_info where Password = '{passw}'")
    data=cur.fetchall()
    conn.close()
    print(data)

while True:
    print(''' Welcome to our Login System
                    Menu
              1. Insert
              2. Update
              3. Search
              4. Delete
              5. Exit
            ''')
    choice = int(input(" Enter Your Choice : "))

    if choice == 1:
        name = input("Enter Username : ")
        password = input("Enter Password : ")
        Cpassword = input("Confirm Password : ")
        if password == Cpassword:
            Insert(name, Cpassword)
            print("Login info saved successfully ")

    elif choice == 2:
        name = input("Enter Username : ")
        password = input("Enter Password : ")
        n = int(input("Now ell me which field you wanted to update\n"
                      "1. Username\n"
                      "2. Password\n"
                      "Enter your choice here : "))
        if n == 1:
            s = "Username"
        else:
            s = "Password"
        newvalue = input("Enter the new Name or Password to Update : ")
        Update(s, name, password, newvalue)
        print("Update successfully.")

    elif choice == 3:
        print("From which option you want to search your data \n "
              "1. By Name \n2. By Password")
        ent = int(input("Enter your choice : "))
        if ent == 1:
            name = input("Enter Username you want to search : ")
            SearchN(name)
        elif ent == 2:
            password = input("Enter Password to verify username : ")
            SearchP(password)

    elif choice == 4:
        name = input("Enter Username : ")
        password = input("Enter Password : ")
        print("Are you sure you want to delete your login informaion?\n"
              "1. Yes\n 2. No")
        n = int(input("Enter your choice"))
        if n == 1:
            Delete(name, password)
            print("Deleted Successfully.")
        else:
            print("You took a good decision.\nThak you!")
    else:
        exit()