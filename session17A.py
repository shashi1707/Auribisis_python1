import mysql.connector as library

class Customer:
    def __init__(self):
        self.id = 0
        self.name= input("Enter Customer name:")
        self.phone= input("Enter Customer phone:")
        self.email=input("Enter Customer email:")

    def showCustomerDetails(self):
        print("{}  | {} | {} ".format(self.name,self.phone,self.email))


print("==Welcome to Customer Software  Management ")
print("Register the Customer")

"""choice = int(input("enter the choice:"))

if choice == 1:
    customer = Customer()
    customer.showCustomerDetails()

    save = input("Would you like to save the data? yes/no:")
    if save == "yes":
        print(">> Connection Created :)")
        sql = "INSERT INTO Customer VALUES('{}' , '{}' , '{}')".format(customer.name, customer.phone, customer.email)
        connection = library.connect(user="root", password="",database ="shashidb",host="127.0.0.1", port="3306")
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        print(">> CUSTOMER SAVED :")
        """


choice = int(input("enter the choice:"))
usage = "yes"
while usage == "yes":
    if choice == 1:
        customers = Customer()
        customers.showCustomerDetails()

        save = input("Would you like to Save Customer? (yes/no): ")
        if save == "yes":

            sql = "INSERT INTO customers VALUES( null,'{}', '{}', '{}')".format(customers.name, customers.phone, customers.email)
            connection = library.connect(user="root", password="", database="shashidb", host="127.0.0.1", port="3306")
            print(">> Connection Created :)")
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()

            print(">> CUSTOMER SAVED :)")

            usage = input("Would You Like Use Software Further? (yes/no): ")





