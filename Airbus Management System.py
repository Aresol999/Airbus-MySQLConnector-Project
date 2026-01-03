import mysql.connector as con
mydb=con.connect(host='localhost',user='root',password='xyz',database='INVENTORY_MANAGEMENT_SYSTEM')
cur=mydb.cursor()
print(mydb.is_connected())

#cur.execute("CREATE database INVENTORY_MANAGEMENT_SYSTEM; USE INVENTORY_MANAGEMENT_SYSTEM;",multi=True)
cur.execute("Create table Inventory( Item_Serial_Number VarChar(300) primary key ,Item_Name VarChar(300) not null,Manufacturing_Company Varchar(300) Not null, Quantity integer not null);")
cur.execute("create table Finished_Products( Product_Serial_Number VarChar(300) primary key ,Product_Type VarChar(300) Not null,Date_Of_Building Date, Quantity integer not null, Status VarChar(300) Not null);")
cur.execute("""create table Orders( Order_ID VarChar(300) primary key, Customer_Name Varchar(300), Product_Serial_Number VarCHar(300) ,Quantity integer not null, Status VarChar(300) not null,FOREIGN KEY (Product_Serial_Number) REFERENCES Finished_Products(PRoduct_Serial_Number)); """)

#Entering sample values for software demo
cur.execute("Insert into Inventory values(%s,%s,%s,%s);",['ENG3201','Engine CFM 56','CFM International',2000])
cur.execute("Insert into Inventory values(%s,%s,%s,%s);",['ENG3202','Engine CFM LEAP','CFM International',4000])
cur.execute("Insert into Inventory values(%s,%s,%s,%s);",['ENG33N1','Engine TRENT 7000','Rolls Royce',600])
cur.execute("Insert into Inventory values(%s,%s,%s,%s);",['ENG3501','Engine TRENT XWB','Rolls Royce',1500])
cur.execute("Insert into Inventory values(%s,%s,%s,%s);",['ENG3801','Engine GP7000','Engine Alliance',300])
cur.execute("Insert into Inventory values(%s,%s,%s,%s);",['GEAR320','Landing Gear (A320)','HAECO',7000])
cur.execute("Insert into Inventory values(%s,%s,%s,%s);",['GEAR33N','Landing Gear (A330neo)','Revima',650])
cur.execute("Insert into Inventory values(%s,%s,%s,%s);",['GEAR350','Landing Gear (A350)','Liebherr Aerospace',1650])
cur.execute("Insert into Inventory values(%s,%s,%s,%s);",['GEAR380','Landing Gear (A380)','UTC Aerospace',350])
cur.execute("Insert into Inventory values(%s,%s,%s,%s);",['ALT1NN','Radio Altimeter','Collins Aerospace',10500])
cur.execute("Insert into Inventory values(%s,%s,%s,%s);",['GYRO5NNN','Gyroscope','MEMS Manufacturers',20500])
cur.execute("Insert into Inventory values(%s,%s,%s,%s);",['BEACON1AA','Beacon lights','Airbus',2000])

cur.execute("Insert into FINISHED_PRODUCTS values('F-GFK','Airbus A320','2007-03-14',40,'Delivered');")
cur.execute("Insert into FINISHED_PRODUCTS values('F-AAA','Airbus A320','2018-11-12',400,'Available');")
cur.execute("Insert into FINISHED_PRODUCTS values('F-AVL','Airbus A320','2021-04-28',205,'Available');")
cur.execute("Insert into FINISHED_PRODUCTS values('D-AIN','Airbus A320','2009-06-03',82,'On Order');")
cur.execute("Insert into FINISHED_PRODUCTS values('VT-EX','Airbus A320','2010-02-13',36,'Delivered');")
cur.execute("Insert into FINISHED_PRODUCTS values('F-WTT','Airbus A330','2022-03-17',90,'Available');")
cur.execute("Insert into FINISHED_PRODUCTS values('CS-TU','Airbus A330','2018-12-11',20,'On Order');")
cur.execute("Insert into FINISHED_PRODUCTS values('OO-AB','Airbus A330','2019-06-04',5,'Delivered');")
cur.execute("Insert into FINISHED_PRODUCTS values('N400DX','Airbus A330','2019-05-14',25,'On Order');")
cur.execute("Insert into FINISHED_PRODUCTS values('D-ANR','Airbus A330','2022-12-13',12,'On Order');")
cur.execute("Insert into FINISHED_PRODUCTS values('A7-AL','Airbus A350','2022-08-04',20,'Available');")
cur.execute("Insert into FINISHED_PRODUCTS values('A7-AN','Airbus A350','2022-08-04',12,'Available');")
cur.execute("Insert into FINISHED_PRODUCTS values('D-AIX','Airbus A350','2017-03-12',52,'On Order');")
cur.execute("Insert into FINISHED_PRODUCTS values('B-189','Airbus A350','2018-11-12',15,'Delivered');")
cur.execute("Insert into FINISHED_PRODUCTS values('OH-LW','Airbus A350','2020-05-16',26,'On Order');")
cur.execute("Insert into FINISHED_PRODUCTS values('9V-SG','Airbus A350','2016-03-12',60,'On Order');")
cur.execute("Insert into FINISHED_PRODUCTS values('9M-MN','Airbus A380','2012-10-13',10,'Available');")
cur.execute("Insert into FINISHED_PRODUCTS values('9V-SK','Airbus A380','2008-07-01',17,'Delivered');")
cur.execute("Insert into FINISHED_PRODUCTS values('A6-EV','Airbus A380','2008-08-03',119,'Delivered');")
cur.execute("Insert into FINISHED_PRODUCTS values('HL761','Airbus A380','2011-03-12',9,'Delivered');")
cur.execute("Insert into FINISHED_PRODUCTS values('D-AIM','Airbus A380','2010-08-18',14,'Delivered');")

cur.execute("Insert into Orders values('AFR189','Air France','F-GFK',40,'Delivered');")
cur.execute("Insert into Orders values('DLH331','Lufthansa','D-AIN',82,'On Order');")
cur.execute("Insert into Orders values('AIC113','Air India','VT-EX',36,'Delivered');")
cur.execute("Insert into Orders values('TAP221','Air Portugal','CS-TU',20,'On Order');")
cur.execute("Insert into Orders values('ABA123','Air Belgium','OO-AB',5,'Delivered');")
cur.execute("Insert into Orders values('DAL002','Delta Air Lines','N400DX',25,'On Order');")
cur.execute("Insert into Orders values('CFG778','Condor','D-ANR',12,'On Order');")
cur.execute("Insert into Orders values('DLH009','Lufthansa','D-AIX',52,'On Order');")
cur.execute("Insert into Orders values('CAL334','Taiwan Air Lines','B-189',15,'Delivered');")
cur.execute("Insert into Orders values('FIN358','Finnair','OH-LW',26,'On Order');")
cur.execute("Insert into Orders values('SIN489','Singapore Airlines','9V-SG',60,'On Order');")
cur.execute("Insert into Orders values('SIN001','Singapore Airlines','9V-SK',17,'Delivered');")
cur.execute("Insert into Orders values('UAE001','Emirates','A6-EV',119,'Delivered');")
cur.execute("Insert into Orders values('KAL001','Korean Air Lines','9V-SK',9,'Delivered');")
cur.execute("Insert into Orders values('DLH001','Lufthansa','D-AIM',14,'Delivered');")
mydb.commit()


mydb=con.connect(host='localhost',user='root',password='delete1t!',database='INVENTORY_MANAGEMENT_SYSTEM')
cur=mydb.cursor()

L_Order_Bids=[]
flag='Y'
while flag=='Y' or flag=='y':
    print("Weclome to AIMS (Airbus Inventory Manegement System)")
    print("Select the information you would like to access or manipulate:")
    print("1. Inventory data")
    print("2. Finished Product data")
    print("3. Orders data")
    print("4.View order bids placed")
    ch=int(input("Enter your choice 1,2,3 or 4: "))
    print('')
    if ch==1:
        print("What operation would you like to perform?")
        print('1. Search for objects in inventory')
        print('2. Search for objects with low quantity')
        ch1=int(input("Enter your choice 1 or 2: "))
        print('')
        if ch1==1:
            print('Enter 1 to search for inventory objects by its serial number')
            print('Enter 2 to search for objects by its name') 
            print('Enter 3 to search for objects by their manufacturing company')
            print('Enter 4 to display entire list of inventory objects')
            ch2=int(input("Enter your choice 1,2 or 3: "))
            print('')
            query=input('Enter criteria to be searched by: ')
            if ch2==1:
                cur.execute('select * from Inventory where Item_Serial_Number = "{}"'.format(query))
                for i in cur:
                    print(i)
                if cur == ():
                    print('No matching records found')
            if ch2==2:
                cur.execute('select * from Inventory where Item_Name = "{}"'.format(query))
                for i in cur:
                    print(i)
                if cur == ():
                    print('No matching records found')
            if ch2==3:
                cur.execute('select * from Inventory where Manufacturing_Company = "{}"'.format(query))
                for i in cur:
                    print(i)
                if cur == ():
                    print('No matching records found')
            if ch2==4:
                cur.execute('select * from Inventory;')
                for i in cur:
                    print(i)
                if cur == ():
                    print('No matching records found')
        elif ch1==2:
            query=int(input("Enter minimum amount of quantity you want to search by: "))
            cur.execute('select * from Inventory where Quantity < {}'.format(query))
            for i in cur:
                print(i)
            if cur == ():
                    print('No matching records found')
    elif ch==2:
        print('What operation would you like to perform? ')
        print('1. Search for finished products by product serial number')
        print("2. Search for finished products by Product Type")
        print('3. Search for finished products by Date of Building ')
        print('4. Search for finished products by Status')
        print('5. Add a finished product into the database')
        ch1=int(input("Enter your choice 1,2,3,4 or 5: "))
        print('')
        if ch1==1:      
            query=input('Enter criteria to be searched by: ')
            cur.execute('select * from Finished_Products where Product_Serial_Number = "{}"'.format(query))
            for i in cur:
                print(i)
            if cur == ():
                    print('No matching records found')
        elif ch1==2:
            query=input('Enter criteria to be searched by: ')
            cur.execute('select * from Finished_PRoducts where Product_Type = "{}"'.format(query))
            for i in cur:
                print(i)
            if cur == ():
                    print('No matching records found')
        elif ch1==3:
            query=input('Enter criteria to be searched by: ')
            cur.execute('select * from Finished_PRoducts where Date_Of_Building = "{}"'.format(query))
            for i in cur:
                print(i)
            if cur == ():
                    print('No matching records found')
        elif ch1==4:
            query=input('Enter criteria to be searched by ( on order/ delivered / available ): ')
            cur.execute('select * from Finished_PRoducts where Status = "{}"'.format(query))
            for i in cur:
                print(i)
            if cur == ():
                    print('No matching records found')
        elif ch1==5:
            a=input('Enter Product Serial Number:')
            b=input('Enter Product type: ')
            c=input('Enter date of building (YYYY-MM-DD): ')
            d=input("Enter quantity of product produced: ")
            e=input("Enter Status of product (on order/ Delivered/ available): ")
            s='insert into Finished_Products values(%s,%s,%s,%s,%s)'
            val=(a,b,c,d,e)
            cur.execute(s,val)
    elif ch==3:
        print("What operation would you like to perform?")
        print('1. Place a bid for an order')
        print('2. View an order ')
        print('3. Delete an order')
        ch1=int(input('Enter your desired operation 1,2 or 3: '))
        print('')
        if ch1==1:
            print('Here is  list of available products')
            cur.execute('Select * from Finished_Products where status="available";')
            for i in cur:
                print(i)
            o1=input('Enter the product serial number you are interested in: ')
            o2=input('Enter your Customer_Id: ')
            o3=input('Enter your Customer_Name: ')
            o4=int(input('Enter your bid (in dollars):'))
            L_Order_Bids.append({'Product_Serial_Number':o1,'Customer_Id':o2,'Customer_Name':o3,'Bid (in Dollars)':o4})
            print('Thank you, Order Bid has succesfully been placed.')
            print('')
        elif ch1==2:
            print('What operation would you like to perform? ')
            print('1. Search for orders by Customer Name')
            print("2. Search for orders by Product Serial Number")
            print('3. Search for orders by Quantity')
            print('4. Search for orders by Status')
            print('5. Search for orders by order ID: ')
            ch2=int(input('Enter your choice 1,2,3,4 or 5: '))
            query=input('Enter criteria to be searched: ')
            print('')
            if ch2==1:
                cur.execute('Select * from Orders where Customer_Name = "{}"'.format(query))
                for i in cur:
                    print(i)
            if ch2==2:
                cur.execute('Select * from Orders where Product_Serial_Number = "{}"'.format(query))
                for i in cur:
                    print(i)
            if ch2==3:
                cur.execute('Select * from Orders where Quantity = {}'.format(query))
                for i in cur:
                    print(i)
            if ch2==4:
                cur.execute('Select * from Orders where Status = "{}"'.format(query))
                for i in cur:
                    print(i)
            if ch2==5:
                cur.execute('Select * from Orders where Order_Id = "{}"'.format(query))
                for i in cur:
                    print(i)
            print('')
        elif ch1==2:
            print('What operation would you like to perform? ')
            print('1. Delete orders by Customer Name')
            print("2. Delete orders by Product Serial Number")
            print('3. Delete orders by Quantity')
            print('4. Delete orders by Status')
            print('5. Delete orders by order ID: ')
            ch2=int(input('Enter your choice 1,2,3,4 or 5: '))
            query=input('Enter criteria to be searched: ')
            print('')
            if ch2==1:
                cur.execute('delete from orders where CUstomer_Name = "{}"'.format(query))
                
            if ch2==2:
                cur.execute('delete from Orders where Product_Serial_Number = "{}"'.format(query))
                
            if ch2==3:
                cur.execute('delete from Orders where Quantity = "{}"'.format(query))
               
            if ch2==4:
                cur.execute('delete from Orders where Status = "{}"'.format(query))
                
            if ch2==5:
                cur.execute('delete from Orders where Order_Id = "{}"'.format(query))
            print('')
    elif ch==4:
        for i in range(0,len(L_Order_Bids)):
            print('Bid Number',i+1)
            print(L_Order_Bids[i])
    flag=input('Enter "Y" or "y" to do more operations: ')
mydb.commit()
