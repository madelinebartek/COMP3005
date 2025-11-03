import psycopg2

dbName = input("Enter the database name: ")
pw = input("Please enter your password: ")

print("Connecting to the database")

#connecting to the database
conn = psycopg2.connect(
    dbname = dbName,
    user="postgres",
    password= pw,
    host="localhost",
    port="5432"
)

cur = conn.cursor()


#getAllStudents() -- all records from the table
def getAllStudents():
    try:
        cur.execute("Select * from students;")
        rows = cur.fetchall()
        for row in rows: 
            print(row)
    except:
        print("Failed to retrieve all students")

#addStudent(first_name, last_name, email, enrollment_date) -- add student to table
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
        conn.commit()
        print("New person added\n")
    except:
        print("Failed to add student " + first_name + last_name )

#updateStudentEmail(student_id, new_email) -- change student email based off student_id
def updateStudentEmail(student_id, new_email):    
    try:
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
        conn.commit()
        print("Email has been updated\n")
    except:
        print("Failed to update email.")


#deleteStudent(student_id) -- delete specific student
def deleteStudent(student_id):
    try:
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id))
        conn.commit()
        print("Student has been deleted\n")
    except:
        print("Failed to delete student " + student_id)


num = -1
#can do several operations before exiting to prevent constantly having to run the program 
while True:

    #while loop for selecting which operation to do
    while True:

        print("[1] Get all students on record")
        print("[2] Add a new student")
        print("[3] Update a student's email")
        print("[4] Delete a student's record")
        print("[0] Exit")

        num = int(input("Select a number: "))
        
        try:
            num >= 0
            num <= 4
            break
        except: 
            print("Number entered isn't valid. Please choose a number between 1 and 4.")
    
    if(num == 0): 
        #will exit the program 
        cur.close()
        conn.close()
        print("Goodbye!")
        break
    elif(num == 1):
        #retrieves all students
        print("Getting all students")
        getAllStudents()
    elif (num == 2):
        #collects values and adds the student
        firstName = input("Enter the student's first name: ")
        lastName = input("Enter the student's last name: ")
        email = input("Enter the student's email: ")
        enroll = input("Enter the student's enrollment date (YYYY-MM-DD): ")
        print("Adding " + firstName + " " + lastName)
        addStudent(firstName, lastName, email, enroll)
    elif (num == 3):
        #collects values and updates their email
        studID = input("Enter the student's ID number: ")
        newEmail = input("Enter the student's new email: ")
        print("Updating %s's email to %s" %(studID, newEmail))
        updateStudentEmail(studID, newEmail)
    elif(num == 4):
        #deletes specified student 
        studID = input("Enter student's id: ")
        print("Deleteing student " + studID)
        deleteStudent(studID)
    num = -1
    print()








