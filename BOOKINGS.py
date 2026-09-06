import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database='piyush12r')
cursor=mydb.cursor()

def addrecord():
    cursor.execute("select * from bookings")
    records=cursor.fetchall()
    for x in records:
        print(x)
    try:
        ch='y'
        while ch=='y':
            ticket_id=input("Enter the id of the ticket eg(1,2,3,...):")
            cursor.execute("Select * from bookings where ticket_id='%s' "%(ticket_id))
            record=cursor.fetchone()
            if record!=None:
                print("Primary key already exits")
                break
            if ticket_id.isdigit():
                continue
            else:
                print("Invalid ID")
                break
            movie_id=int(input("Enter the id of the movie to be booked:"))
            date=input("Enter the date of booking(YYYY-MM-DD):")
            no=int(input("Enter the no of tickets to be bought:"))
            query="INSERT INTO bookings VALUES({0},{1},'{2}',{3})".format(ticket_id,movie_id,date,no)
            cursor.execute(query)
            mydb.commit()
            print("--------Record(s) added --------")
            cursor.execute("select * from bookings")
            records=cursor.fetchall()
            for x in records:
                print(x)
            ch=input("Want to add more records:")
    except Exception as e:
        print(e)

def delrecord():
    cursor.execute("select * from bookings")
    records=cursor.fetchall()
    for x in records:
        print(x)
    try:
        id=int(input("Eneter the id of the ticket whose record is to be deleted eg(1,2,3,...):"))
        query="DELETE FROM bookings WHERE ticket_id={}".format(id)
        cursor.execute(query)
        print("----------Record deleted----------")
        cursor.execute("select * from bookings")
        records=cursor.fetchall()
        for x in records:
            print(x)
        mydb.commit
        mydb.close()
    except Exception as e:
        prinjt(e)

def displayrecord():
    cursor.execute("select * from bookings")
    records=cursor.fetchall()
    for x in records:
        print(x)

def searchrecord():
    cursor.execute("select ticket_id from bookings")
    records=cursor.fetchall()
    for x in records:
        print(x)
    try:
        id=int(input("Enter the id of the ticket to search eg(1,2,3,...):"))
        query="select * from bookings where ticket_id="+str(id)
        cursor.execute(query)
        myrecord=cursor.fetchone()
        if myrecord != None:
            print(myrecord)
        else:
            print("No such Ticket found")
    except Exception as e:
        print(e)
        
def updaterecord():
    cursor.execute("select * from bookings")
    records=cursor.fetchall()
    for x in records:
        print(x)
    try:
        id=int(input("Enter the id of the ticket to be updated eg(1,2,3,...):"))
        query="select * from bookings where ticket_id={}".format(id)
        cursor.execute(query)
        myrecord=cursor.fetchone()
        if myrecord != None:
            print("----------Record Found-Details are------------")
            print(myrecord)
        choice=input("Do you want to change booking date(y/n):")
        if choice=='y':
            date=input("Enter new booking date(YYYY-MM-DD):")
            if date.startswith('2025'):
                print("Enter the valid booking date!!")
            query="UPDATE bookings set booking_date='{}' where ticket_id={}".format(date,id)
            cursor.execute(query)
            mydb.commit()
            print("----------Record(s) Updated-----------")
        else:
            print("No such Ticket exists")
            mydb.close()

            choice=input("Do you want to update no. of tickets(y/n):")
            if choice=='y':
                ntickets=input("Enter new  no. of tickets to be bought:")
                query="UPDATE bookings set ntickets={} where ticket_id={}".format(ntickets,id)
                cursor.execute(query)
                mydb.commit()
                print("----------Record(s) Updated-----------")
                cursor.execute("select * from bookings")
                records=cursor.fetchall()
                for x in records:
                    print(x)
            else:
                print("No such Ticket exists")
                mydb.close()
    except Exception as e:
        print(e)

def bookings():
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

bookings()
