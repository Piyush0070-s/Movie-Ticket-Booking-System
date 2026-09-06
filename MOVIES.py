import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database='piyush12r')
cursor=mydb.cursor()

def addrecord():
    cursor.execute("select * from movies")
    records=cursor.fetchall()
    for x in records:
        print(x)
    try:
        ch='y'
        while ch=='y':
            movie_id=input("Enter the id of the movie eg(101,..):")
            cursor.execute("Select * from movies where movie_id='%s' "%(movie_id))
            record=cursor.fetchone()
            if record!=None:
                print("Primary key already exits")
                break
            if movie_id=="":
                print("ID of the movie cannot be null")
                break
            hall_id=int(input("Enter the id of the hall:"))
            name=input("Enter the name of the movie:")
            if name=="":
                print("Name of the movie cannot be null")
                break
            duration=int(input("Enter the duration of movie(in min):"))
            type=input("Enter the type of the movie:")
            release=input("Enter the release date of the movie(YYYY-MM-DD):")
            query="INSERT INTO movies VALUES({0},{1},'{2}',{3},'{4}','{5}')".format(movie_id,hall_id,name,duration,type,release)
            cursor.execute(query)
            mydb.commit()
            print("--------Record(s) Added --------")
            cursor.execute("select * from movies")
            records=cursor.fetchall()
            for x in records:
                print(x)
            ch=input("Want to add more records:")
    except Exception as e:
        print(e)
        
def delrecord():
    cursor.execute("select * from movies")
    records=cursor.fetchall()
    for x in records:
        print(x)
    try:
        id=input("Eneter the id of the movie whose record is to be deleted eg(101,..):")
        query="DELETE FROM movies WHERE movie_id='{}' ".format(id)
        cursor.execute(query)
        print("----------Record Deleted----------")
        cursor.execute("select * from movies")
        records=cursor.fetchall()
        for x in records:
            print(x)
        mydb.commit()
        mydb.close()
    except Exception as e:
        print(e)

def displayrecord():
    cursor.execute("select * from movies")
    records=cursor.fetchall()
    for x in records:
        print(x)
    

def searchrecord():
    cursor.execute("select movie_id from movies")
    records=cursor.fetchall()
    for x in records:
        print(x)
    try:
        id=int(input("Enter the id of the movie to search eg(101,..):"))
        query="select * from movies where movie_id="+str(id)
        cursor.execute(query)
        myrecord=cursor.fetchone()
        if myrecord != None:
            print(myrecord)
        else:
            print("No such Movie found")
    except Exception as e:
        print(e)

def updaterecord():
    cursor.execute("select * from movies")
    records=cursor.fetchall()
    for x in records:
         print(x)
    try:
        id=int(input("Enter the id of the movie to be updated eg(101,..):"))
        query="select * from movies where movie_id={}".format(id)
        cursor.execute(query)
        myrecord=cursor.fetchone()
        if myrecord != None:
            print("----------Record Found-Details are------------")
            print(myrecord)
            choice=input("Do you want to update the release date(y/n):")
            if choice=='y':
                release=input("Enter new updated release date(YYYY-MM-DD):")
                query="UPDATE movies set release_date='{} 'where movie_id={}".format(release,id)
                cursor.execute(query)
                mydb.commit()
                print("----------Record(s) Added-----------")
                cursor.execute("select * from movies")
                records=cursor.fetchall()
                for x in records:
                    print(x)
        else:
            print("No such Movie exists")
        mydb.close()
    except Exception as e:
        print(e)

def movies():
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

movies()




        
