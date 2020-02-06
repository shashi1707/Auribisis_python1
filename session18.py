import mysql.connector as library

class Customer:
    def __init__(self,mode):
        if mode == 1:
            self.id = 0
            self.name = input("Enter Customer name:")
            self.phone = input("Enter Customer phone:")
            self.email = input("Enter Customer email:")
        elif mode == 2:
            self.id = int(input("Enter the ID:"))
            self.name = input("Enter Customer name:")
            self.phone = input("Enter Customer phone:")
            self.email = input("Enter Customer email:")
        else:
            pass


    def showCustomerDetails(self):
        print("{}| {}  | {} | {} ".format(self.id,self.name,self.phone,self.email))


print("==Welcome to Customer Software  Management==== ")
print("1.Register the Customer")
print("2. Update the Existing  customer")
print("3. delete the Existing  customer")
print("4. View All customers")
print("5. View customer by ID")
print("6. View Customer by  Phone")

def executeOperation(sql):
    connection = library.connect(user="root", password="", database="shashidb", host="127.0.0.1", port="3306")
    print(">> Connection Created :)")
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


choice = int(input("enter the choice:"))
usage = "yes"
while usage == "yes":
    if choice == 1:
        customers = Customer(1)
        customers.showCustomerDetails()

        save = input("Would you like to Save Customer? (yes/no): ")
        if save == "yes":

            sql = "INSERT INTO customers VALUES( null,'{}', '{}', '{}')".format(customers.name, customers.phone, customers.email)

            """connection = library.connect(user="root", password="", database="shashidb", host="127.0.0.1", port="3306")
            print(">> Connection Created :)")
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()"""
            executeOperation(sql)

            print(">> CUSTOMER SAVED :)")

            usage = input("Would You Like Use Software Further? (yes/no): ")


    elif choice == 2:

        customers = Customer(2)
        customers.showCustomerDetails()

        save = input("Would you like to Save Customer? (yes/no): ")

        if save == "yes":

            sql = "update customers set name = '{}',phone = '{}',email='{}' where id ={}".format(customers.name,customers.phone,customers.email,customers.id)

            """connection = library.connect(user="root", password="", database="shashidb", host="127.0.0.1", port="3306")
            print(">> Connection Created :)")
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()"""
            executeOperation(sql)

            print(">> CUSTOMER SAVED :)")

            usage = input("Would You Like Use Software Further? (yes/no): ")

    elif choice == 3:


        delete = input("Would you like to delete Customer? (yes/no): ")
        id = int(input("Enter the id of customer to be deleted:"))
        if delete == "yes":

            sql = "delete from customers where id ={}".format(id)
            """connection = library.connect(user="root", password="", database="shashidb", host="127.0.0.1", port="3306")
            print(">> Connection Created :)")
            cursor = connection.cursor()
            cursor.execute(sql)"""
            executeOperation(sql)

            print("CUSTOMER DELETED:")


            usage = input("Would You Like Use Software Further? (yes/no): ")


    elif choice == 4:
        sql = "select * from Customers"
        connection = library.connect(user="root", password="", database="shashidb", host="127.0.0.1", port="3306")
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("Showing the data in List of Tuple")
        for row in rows:
            print(row)

        print(">>>>>Showing the data as object-data<<<<<< ")
        for row in rows:
            customers = Customer(3)
            customers.id = row[0]
            customers.name = row[1]
            customers.phone = row[2]
            customers.email = row[3]

            customers.showCustomerDetails()

        usage = input("Would You Like Use Software Further? (yes/no): ")

    elif choice == 5:
        id = int(input("Enter the Customer ID to be Searched: "))
        sql = "select * from Customers where id = {}".format(id)
        connection = library.connect(user="root", password="", database="shashidb", host="127.0.0.1", port="3306")
        cursor = connection.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
       # print(row)
        if row is not None:
            print(row)
        else:
            print("INVALID ID")

        usage = input("Would You Like Use Software Further? (yes/no): ")

    elif choice == 6:
        phone = input("Enter the Customer Phone to be Searched: ")
        sql = "select * from Customers where phone = '{}'".format(phone)
        connection = library.connect(user="root", password="", database="shashidb", host="127.0.0.1", port="3306")
        cursor = connection.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        if row is not None:
            print(row)
        else:
            print("INVALID PHONE")

        usage = input("Would You Like Use Software Further? (yes/no): ")