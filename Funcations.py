import connection
#check emplopy is exist or not
def Check_Employee(emp_id):
    sql = "SELECT * FROM employeerecord WHERE id = %s"
    c = connection.con.cursor(buffered=True)
    data = (emp_id,)
    
    c.execute(sql,data)
    rowcount = c.rowcount
    
    if rowcount == 1:
        return True 
    else:
        return False
    
    
    #add emplopye
def Add_Emplpye():
    id = input("Enter ID: ")
        
    if(Check_Employee(id) == True):
        print("-----------------------------------------------")
        print("Employee already exists\nTry Again\n")
        print("-----------------------------------------------\n")
        menu()
    else:
        name = input("Enter Name: ")
        post = input("Enter Post: ")
        salary = input("Enter Salary: ")
        data = (id,name,post,salary)
        sql = "INSERT INTO employeerecord(id,name,post,salary) VALUES(%s,%s,%s,%s)"
        c = connection.con.cursor()
        c.execute(sql,data)
        connection.con.commit()
        print("-----------------------------------------------")
        print("Employee Added Successfully\n")
        print("-----------------------------------------------")
        
        


# Function to Remove Employee with given Id

def Remove_Employee():
    id = input("Enter ID: ")
        
    if(Check_Employee(id) == False):
        print("-----------------------------------------------")
        print("Employee does not  exists\nTry Again\n")
        print("-----------------------------------------------")
        menu()
    else:
        sql = 'delete from employeerecord where id = %s'
        data = (id,)
        c = connection.con.cursor()
        c.execute(sql,data)
        connection.con.commit()
        print("-----------------------------------------------")
        print("Employee Removed successfully\n")
        print("-----------------------------------------------")
        
        
# Function to Promote Employee
def Promote_Employee():
    id = input("Enter ID: ")
    
    if(Check_Employee(id) == False):
        print("-----------------------------------------------")
        print("Employee does not  exists\nTry Again\n")
        print("-----------------------------------------------")
        
        
    else:
        Amount = int(input("Enter increase in Salary : "))
        sql = "UPDATE employeerecord SET salary = salary + %s WHERE id = %s"
        data = (Amount,id)
        c = connection.con.cursor()
        c.execute(sql,data)
        connection.con.commit()
        print("-----------------------------------------------")
        print("Employee Promoted successfully")
        print("-----------------------------------------------")
        

# Function to Display all Employees
def Display_Employee():
    sql = "SELECT * FROM employeerecord"
    c = connection.con.cursor()
    c.execute(sql)
    data = c.fetchall()
    
    for i in data:
        print("Employee Id : ", i[0])
        print("Employee Name : ", i[1])
        print("Employee Post : ", i[2])
        print("Employee Salary : ", i[3])
        print("-----------------------------\
        -------------------------------------\
        -----------------------------------")
     
#menu function
def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Display Employees")
    print("2 to Exit")
    print("3 for admin-login")
    
    while True:
    
        choice = int(input("Enter your Choice "))
        if choice == 1:
            Display_Employee()
            
        elif choice == 2:
            print("-----------------------------------------------")
            print("Thank You for using Employee Management Record ")
            print("Good Bye")
            print("-----------------------------------------------")
            break
            
        elif choice == 3:
            email = input("Enter email: ")
            password = input("Enter password: ")
            if admin_auth(email,password):
                print("Login Successfull")
                print("Welcome to Admin Panel")
                print("-----------------------------------------------")
                
                while True:
                    print("Press ")
                    print("1 to Add Employee")
                    print("2 to Promote Employee")
                    print("3 to Remove Employee")
                    print("4 to Display Employees")
                    print("5 to Exit")
                    
                    choice = int(input("Enter your Choice "))
                    
                    if choice == 1:
                        Add_Emplpye()
                    elif choice == 2:
                        Promote_Employee()
                    elif choice == 3:
                        Remove_Employee()
                    elif choice == 4:
                        Display_Employee()
                    elif choice == 5:
                        exit()    
                    else:
                        print("Invalid Choice")    
            else:
                print("Invalid email or password")        
        else:
            print("Invalid Choice")   
        
#admin login 
def admin_auth(email,password):
    sql = "SELECT * FROM admin"
    c = connection.con.cursor()
    c.execute(sql)
    data = c.fetchall()
    
    admin_email=data[0][1]
    admin_password=data[0][2]
    if(email==admin_email and password==admin_password):
        return True
    else:
        return False