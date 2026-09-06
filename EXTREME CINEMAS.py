import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database='piyush12r')
cursor=mydb.cursor()

def menu():
    while True:
        print("--------------------EXTREME CINEMAS----------------------")
        print("1.Cinema Halls")
        print("2.Movies")
        print("3.Bookings")
        print("4.Exit")
        print("---------------------------------------------------------------------")

        choice=int(input("Enter your choice:"))
        if choice==1:
            print("--------------------CINEMA HALLS--------------------")
            import CINEMAHALLS
        elif choice==2:
            print("-------------------MOVIES-------------------")
            import MOVIES
        elif choice==3:
            print("------------------BOOKINGS-------------------")
            import BOOKINGS
        elif choice==4:
            print("Exiting")
            break
        else:
            print("Wrong Input")

menu()


