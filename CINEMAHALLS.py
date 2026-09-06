import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database='piyush12r')
cursor=mydb.cursor()

def addrecord():
    try:
        cursor.execute("select * from cinema_halls")
        records=cursor.fetchall()
        for x in records:
            print(x)
        ch='y'
        while ch=='y':
            hall_id=input("Enter the id of the cinema hall eg(1,2,3...):")
            cursor.execute("Select * from cinema_halls where hall_id='%s' "%(hall_id))
            record=cursor.fetchone()
            if record!=None:
                print("Primary key already exits")
                break
            if hall_id.isdigit():
                continue
            else:
                print("Invalid Hall id")
                break
            hall_name=input("Enter the name of the cinema hall:")
            if hall_name=="":
                print("Hall Name cannot be null")
                break
            if hall_name.isalpha():
                continue
            else:
                print("Invalid hall name ")
                break
            seats=int(input("Enter the no. of seats in cinema hall:"))
            screen=input("Enter the screen type of cinema hall(2D,3D,IMAX):")
            if screen=="":
                print("Screen type cannot be null")
                break
            location=input("Enter the location of cinema hall:")
            query="INSERT INTO cinema_halls VALUES({0},'{1}',{2},'{3}','{4}')".format(hall_id,hall_name,seats,screen,location)
            cursor.execute(query)
            mydb.commit()
            print("--------Record(s) Added --------")
            cursor.execute("select * from cinema_halls")
            records=cursor.fetchall()
            for x in records:
                print(x)
            ch=input("Want to add more records(y/n):").isupper
    except Exception as e:
        print(e)

def delrecord():
            cursor.execute("select * from cinema_halls")
            records=cursor.fetchall()
            for x in records:
                print(x)
            try:
                id=input("Eneter the id of the hall whose record is to be deleted eg(1,2,3...):")
                query="DELETE FROM cinema_halls WHERE hall_id='{}' ".format(id)
                cursor.execute(query)
                print("Record Deleted")
                cursor.execute("select * from cinema_halls")
                records=cursor.fetchall()
                for x in records:
                    print(x)
                mydb.commit()
                mydb.close()
            except Exception:
                print("First delete the desired data from parent row of movies table." )

def displayrecord():
    cursor.execute("select * from cinema_halls")
    records=cursor.fetchall()
    for x in records:
        print(x)
    

def searchrecord():
    cursor.execute("select hall_id from cinema_halls")
    records=cursor.fetchall()
    for x in records:
                print(x)
    try:
        id=int(input("Enter the id of the hall to search  eg(1,2,3...):"))
        query="select *from cinema_halls where hall_id="+str(id)
        cursor.execute(query)
        myrecord=cursor.fetchone()
        if myrecord != None:
                print(myrecord)
        else:
                print("No such Cinema Hall found")
    except Exception as e:
        print(e)

def updaterecord():
        cursor.execute("select * from cinema_halls")
        records=cursor.fetchall()
        for x in records:
                print(x)
        try:
            id=int(input("Enter the id of the hall to be updated  eg(1,2,3...):"))
            query="select * from cinema_halls where hall_id={}".format(id)
            cursor.execute(query)
            myrecord=cursor.fetchone()
            if myrecord != None:
                print("----------Record Found-Details are------------")
                print(myrecord)
                choice=input("Do you want to update no. of seats(y/n):")
                if choice=='y':
                        seats=int(input("Enter new updated no. of seats:"))
                        query="UPDATE cinema_halls set seats={} where hall_id={}".format(seats,id)
                        cursor.execute(query)
                        mydb.commit()
                        print("----------Record(s) Updated-----------")
                        cursor.execute("select * from cinema_halls")
                        records=cursor.fetchall()
                        for x in records:
                            print(x)
                else:
                        print("No such Cinema Hall exists")
                mydb.close()
        except Exception as e:
                print(e)

def cinemahall():
        while True:
                print("1.Add record")
                print("2.Delete record")
                print("3.Display record")
                print("4.Search record")
                print("5.Update record")
                print("6.Back to main menu")
        
                ch=int(input("Enter your choice:"))
                if ch==1:
                    addrecord()
                elif ch==2:
                    delrecord()
                elif ch==3:
                    displayrecord()
                elif ch==4:
                    searchrecord()
                elif ch==5:
                    updaterecord()
                elif ch==6:
                    break
                else:
                    print("Wrong Input")

cinemahall()

