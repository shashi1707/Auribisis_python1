import mysql.connector as library

class DataBase:

    def __init__(self):
        self.connection = library.connect(user="root", password="", database="shashidb", host="127.0.0.1", port="3306")
        print("Connection Created:)")
    def executeWriteOperation(self,sql):

        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        print("SQL executec")

    def executeReadOperation(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

database=DataBase()

class Customer:

    def __init__(self,mode):
        if mode == 1:
            self.id = 0
            self.name = input("Enter the customer name: ")
            self.phone = input("Enter the customer phone: ")
            self.email = input("Enter the customer email:")

        elif mode == 2:
            self.id = int(input("Enter the Customer ID: "))
            self.name= input("Enter the customer name: ")
            self.phone = input("Enter the customer phone: ")
            self.email = input("Enter the customer email: ")
        else:
            pass

    def showCustomerDetails(self):
        print("{} | {} | {} | {} ".format(self.id,self.name,self.phone, self.email))

def main():
    repeat = "yes"
    while repeat == "yes":
        print("==Welcome to Customer Software  Management==== ")
        print("1.Register the Customer")
        print("2. Update the Existing  customer")
        print("3. delete the Existing  customer")
        print("4. View All customers")
        print("5. View customer by ID")
        print("6. View Customer by  Phone")

        choice = int(input("enter the choice:"))

        if choice == 1:
            customers = Customer(1)
            customers.showCustomerDetails()

            save = input("Would you like to Save Customer? (yes/no): ")
            if save == "yes":
                sql = "INSERT INTO customers VALUES( null,'{}', '{}', '{}')".format(customers.name, customers.phone,
                                                                                    customers.email)
                database.executeWriteOperation(sql)
                print(">> CUSTOMER SAVED :)")


        elif choice == 2:

            customers = Customer(2)
            customers.showCustomerDetails()

            save = input("Would you like to Save Customer? (yes/no): ")

            if save == "yes":
                sql = "update customers set name = '{}',phone = '{}',email='{}' where id ={}".format(customers.name,
                                                                                                     customers.phone,
                                                                                                     customers.email,
                                                                                                     customers.id)
                database.executeWriteOperation(sql)

                print(">> CUSTOMER SAVED :)")



        elif choice == 3:

            delete = input("Would you like to delete Customer? (yes/no): ")
            id = int(input("Enter the id of customer to be deleted:"))
            if delete == "yes":
                sql = "delete from customers where id ={}".format(id)

                database.executeWriteOperation(sql)

                print("CUSTOMER DELETED:")




        elif choice == 4:
            sql = "select * from Customers"
            rows=database.executeReadOperation(sql)
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


        elif choice == 5:
            id = int(input("Enter the Customer ID to be Searched: "))
            sql = "select * from Customers where id = {}".format(id)
            rows = database.executeReadOperation(sql)
            # print(row)
            if rows is not None:
                print(rows)
            else:
                print("INVALID ID")



        elif choice == 6:
            phone = input("Enter the Customer Phone to be Searched: ")
            sql = "select * from Customers where phone = '{}'".format(phone)
            rows = database.executeReadOperation(sql)
            if rows is not None:
                print(rows)
            else:
                print("INVALID PHONE")

        else:
            print("Enter the valid Choice")

        repeat = input("Would You Like Use Software Further? (yes/no): ")
if __name__ == "__main__":
    main()