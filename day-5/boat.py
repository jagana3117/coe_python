import mysql.connector as c
mydb =c.connect(
  host="localhost",
  user="root",
  password="1234",
  database="retail"
)
mycursor = mydb.cursor()
# mycursor.execute("create table boat(bid int primary key,bname varchar(30),city varchar(30))")
# mycursor.execute("""
#     ALTER TABLE boat
#     ADD COLUMN year INT
# """)
option=input("Enter your operation on boat table: ")
if option=='insert':
    bid = int(input("Enter boat id: "))
    bname = input("Enter boat name: ")
    year = input("Enter year: ")
    mycursor.execute("INSERT INTO boat (bid, bname, year) VALUES (%s, %s, %s)", (bid, bname, year))
elif option=='update':
    bid = int(input("Enter boat id: "))
    bname = input("Enter boat name: ")
    year = input("Enter year: ")
    mycursor.execute("update boat set bname=%s, year=%s where bid=%s",(bname,year,bid))
elif option=='delete':
    bid = int(input("Enter boat id: "))
    mycursor.execute("delete from boat where bid=%s")
elif option=='select':
    mycursor.execute(("select * from boat"))
    details=mycursor.fetchall()
    for bt in details:
        print(bt)
elif option=='more than 18k':
    mycursor.execute("select bid,bname from boat where price>18000")
    details = mycursor.fetchall()
    for bt in details:
        print(bt)
elif option=='order':
    mycursor.execute("select * from boat order by  bid asc")
    details = mycursor.fetchall()
    for bt in details:
        print(bt)
elif option=='city hyd':
    mycursor.execute("select * from boat where city='hyd'")
    details = mycursor.fetchall()
    for bt in details:
        print(bt)
elif option=='max':
    mycursor.execute("select max(price),bid,bname from boat")
    details = mycursor.fetchall()
    for bt in details:
        print(bt)
elif option=='min':
    mycursor.execute("select min(price),bid,bname from boat")
    details = mycursor.fetchall()
    for bt in details:
        print(bt)
mydb.commit()