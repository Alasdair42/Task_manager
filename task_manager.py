# let LoggedIn equal False
loggedIn = False

# Creat an empty file called username to store username data
username = ""
# Creat an empty file called password to store password data
password = ""

# Open user txt file to read the data
user_file = open("user.txt", "r")

#use a for loop to loop through the data in the user.txt file
for line in user_file:
    # Use strip to remove punctuation at the start and end of line and save in variable temp
    temp = line.strip()
    # Use split to split the data in each line on the comma into characters
    temp = temp.split(",")

    # Each user name added assign it to temp[o]
    username += temp[0]
    # Each psss word added assign it to temp[1]
    password += temp[1]

# Close the file
user_file.close()

# Use a while loop and let it equal False for incorrect username or password
while loggedIn == False:
    
    # Aske user to enter a user name and save as userLoggin
    userLoggin = input(" Please enter your username: ")
    # Ask user to enter a pass word and save as userPass
    userPass = input(" Please enter your password: ")

    # Use an if statement with not in if user name is not stored in username or user uses a space
    if userLoggin not in username or userLoggin == " ":
        # Print statement
        print(" Username not found ")
        # LoggedIn is still False so the loop will still run
        loggedIn = False

    # Use elif statement if pass word is not stored in password or user uses a space
    elif userPass not in password or userPass == " ":
        
        print(" Incorrect password ")
        # LoggedIn still False so the while loop will still run 
        loggedIn = False

    # Use elif statement with in, if user name and pass word are stored in username and password
    elif userLoggin in username and userPass in password:
        print(f" Welcome {userLoggin} you are logged in ")
        # LoggedIn is now True so the code exits the loop
        loggedIn = True
    
while loggedIn == True:

    # use an if statement for when the user inputs admin
    if userLoggin == "admin":
        # Print a statement where the user has the choice to add a new user
        print(""" Please make a selection from the following:
 r - register a new user
 a - assign a new task
 va - viewall user assigned tasks
 vm - view my assigned tasks
 s - statistics
 e - exit """)
    # Use else statement to print a statement where the user can not register a new user    
    else:
       print(""" Please make a selection from the following:
 a - assign a new task
 va - viewall user assigned tasks
 vm - view my assigned tasks
 e - exit """) 
        
    # choice is saved as the choice the user inputs
    choice = input(" ")
    
    # Use the if statement if the user enters r as the choice
    if choice == "r":
        # Let new_log equal False
        new_log = False
        # Use a while loop for when the newuser already exists in the data base
        while new_log == False:
            # Aske user to enter a new name and save as newuser
            newuser = input(" Please enter a new name: ")
            # Use if statement if the user is alread in the data base
            if newuser in username:
                # Use f string to output newuser exists in the data base
                print(f" {newuser} exists within the data base ")
                # New_log equals Ralse so the loop will continue
                new_log = False
            # Use if statement when newuser is not in username
            if newuser not in username:
                # Use f string to output newuser does not exist in the data base
                print(f" {newuser} is not in the data base ")
                # New_log equals True so code will exit loop and continue
                new_log = True
            
        # Ask user to input a new password and save as newpass
        newpass = input(" Please enter a new password: ")
        # Ask the user to confirm the password and save as passconfirm
        passconfirm = input(" Please re enter your password: ")

        # use if statement when the passconfirm is the same as the newpass
        if newpass == passconfirm:
            # open the user.txt file and append data to it
            user_file = open("user.txt", "a")
            # using a f string to write the new username to the user text file
            user_file.write(f" \n{newuser} ,")
            # using a fstring to write the new password to the user text file 
            user_file.write(f" {newpass} ")
            # Use f string to print the conformation of the new user neing added to the  user text file
            print(f" Confirmed: {newuser} has been added to the database")
            # Close the file
            user_file.close()

            # Open user txt file to read the data
            user_file = open("user.txt", "r")

            #use a for loop to loop through the data in the user.txt file
            for line in user_file:
                # Use strip to extract the data line by line and remove any punctuation at the start and end of the line and save in variable temp
                temp = line.strip()
                # Use split to split the data in each line at the comma and save it in the variable temp
                temp = temp.split(",")

                # Each user name added assign it to temp[o]
                username += temp[0]
                # Each psss word added assign it to temp[1]
                password += temp[1]

            # Close the file
            user_file.close() 
        
        # Use else statement if newpass is not the same as passconfirm
        else:
            print(" Your passwords do not match ")
    
    # Use the if satatement when the user enter a
    if choice == "a":
        # Import  the function date to use date.today() to set todays date
        from datetime import date
        # Let user_log equal False
        user_log = False

        # Use a while loop for entering a user to assigne a task to
        while user_log == False:
            # Ask the user to enter a name to assigne the task to and save as variable newuser1
            newuser1 = input(" Please enter a user to assign this task to: ")
            #Use if statement when the name is not in the data base
            if newuser1 not in username:
                # Use f string to output newuser1 does not exist in the data base
                print(f" {newuser1} does not exist within our data base ")
                # User_log equals false so the while loop will continue
                user_log = False
            # Use an if statement when the newuser1 is in the database
            if newuser1 in username:
                # use f string to output newuser does exist in data base
                print(f" {newuser1} exists within our data base ")
                # User_log equals true so the code exits out the while loop and continues
                user_log = True
                
        # Ask user to enter a new task and save it as task
        newtask = input(" Please enter a new task: ")
        # Ask user to enter a task description and save as newtaskdes
        newtaskdes = input(" Please enter a task description: ")
        # Use date.today to select todays date and .strftime to output the day, month, year as a string
        newdateass = date.today().strftime("%d-%b-%Y")
        # Ask the user to enter the date the task will be complete and save as newdatcom
        newdatcom = input(" Please enter a date the task will be complete: ")
        # is the task complete will be hard coded as no
        newtaskcom = "No"

        # Open the tasks.txt file and append the new data to it
        task_file = open("tasks.txt", "a")
        # Write the newuser1 to a new line in tasks.txt
        task_file.write(f"\n{newuser1} ,")
        # Write the newtask to a new line in tasks.txt
        task_file.write(f" {newtask} ,")
        # Write the newtaskdes to a new line in tasks.txt
        task_file.write(f" {newtaskdes} ,")
        # Write the newdateass to a new line in tasks.txt
        task_file.write(f" {newdateass} ,")
        # Write the newdatcom to a new line in tasks.txt
        task_file.write(f" {newdatcom} ,")
        # Write the newtaskcom to a new line in tasks.txt
        task_file.write(f" {newtaskcom} ")
        # Print the new task ahs been assigned to the user
        print(f" Confirmed: {newtask} has been assigned to {newuser1} ")
        # Close the file task.txt
        task_file.close()
        
    # Use if statement when user enters va
    if choice == "va":
        # Open task txt file to read the data
        tasks_file = open("tasks.txt", "r")
        #use a for loop with line  to loop through the data line by line in the task.txt file
        for line in tasks_file:
            # Use strip to remove the punctuation at the start and end of line and save in variable temp1
            temp1 = line.strip()
            # Use split to split the data in each line on the comma and save it in temp1
            temp1 = temp1.split(",")
            # Print the data in a f string to output the data
            print(f""" Assigned to:              {temp1[0]}
 Task:                    {temp1[1]}
 Date assigned:           {temp1[3]}
 Due date:                {temp1[4]}
 Task Complete?:          {temp1[5]}
 Task Description:        {temp1[2]}\n """)
        
        # Close the file
        tasks_file.close()

    # Use if statement when user enters vm
    if choice == "vm":
        tasks_file = open("tasks.txt", "r")
        #use a for loop to loop through the data in the task.txt file
        for line in tasks_file:
            # Use strip to remove the puctuation at the start and the end of the line and save in variable temp1
            temp1 = line.strip()
            # Use split to split the data in each line on the comma and save it in temp1
            temp1 = temp1.split(",")
            # Use an if statement with in to check whether userLoggin is in temp1[0]
            if userLoggin in temp1[0]:
                # Print data in a f string to output the data for the userLoggin
                print(f""" Assigned to:              {temp1[0]}
 Task:                    {temp1[1]}
 Date assigned:           {temp1[3]}
 Due date:                {temp1[4]}
 Task Complete?:          {temp1[5]}
 Task Description:        {temp1[2]}\n""")
        
        # Close the file
        tasks_file.close()

    # Use if statement when user enters s
    if choice == "s":
        # Let task_count equal 0
        task_count = 0
        # Open the task.txt file and save it as the variable task_file
        tasks_file = open("tasks.txt", "r")
        #use a for loop to loop through the data line by line in the task.txt file
        for line in tasks_file:
            # Use strip to remove punctuation at the start and the end of the line save in variable temp1
            temp1 = line.strip()
            # Use split to split the data in each line on the comma and save it in temp1
            temp1 = temp1.split(",")
            # let the task_count increase by 1 with each loop
            task_count = task_count + 1

        # print a f string output the total count for the tasks
        print(f" The total number of tasks is: {task_count} ")

        # Close the file
        tasks_file.close()

        # Set the user_count to zero
        user_count = 0
        # Open the user.txt file and save it as the variable user_file
        user_file = open("user.txt", "r")
        #use a for loop to loop through the data line by line in the user.txt file
        for line in user_file:
            # Use strip to remove the punctuation at the start and the end of the line and save in variable temp1
            temp1 = line.strip()
            # Use split to split the data in each line on the comma and save it in temp1
            temp1 = temp1.split(",")
            # let the user_count increase by 1 with each loop
            user_count = user_count + 1
            
       # Print with an f string to output the total count for the users 
        print(f" The total number of users is: {user_count}\n ")

        # Close the file
        user_file.close()
            
    # Use the if statement when the user selects e to exit the program 
    if choice == "e":
        # Print a f string to output user is exiting code
        print(f" Cofirmed {userLoggin} exiting program ")
        #LoggedIn equals False will exit the code 
        loggedIn = False 
            
        
    
              



