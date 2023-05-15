# CA341 Phonebook

## How to compile/execute
### C

There is a Makefile included with the source C file.  
#### Compiling
Entering `make all` into the terminal will both compile and run the code.  
Entering `make build` into the terminal will only compile the code  
If *make* is not installed, the code can be compiled by entering `gcc -o compare compare.c` into the terminal  

#### Executing
The code can be executed by entering `make all` into the terminal  
If `make build` was entered first, `make run` can be entered into the terminal to execute the program.  
If *make* is not installed, the code can be executed by entering `./compare` into the terminal after compiling  

### Python
To execute the python code `python3 compare.py` can be entered in the terminal 

## How to use

### Constraints
Phone numbers are not able to start with any zeros at the start due to how storing phone numbers is implemented.

### Prompt given to the user
```console
1. Add a new contact
2. Delete a contact
3. Search for a contact (by name)
4. Search for a contact (by number)
5. Print the phonebook
6. Exit
```

### Adding a contact
To add a contact, press 1 and then enter. You will then have to input the name, phone number and address for the new contact. The contact will then be added.

### Deleting a contact
To delete a contact, press 2 and then enter. You will then have to input the name for the contact to be deleted. The contact will then be found and deleted.

### Search for a contact (by name)
To search a contact by the contact's name, press 3 and then enter. You will then have to input the name for the contact you would like to search for. The contact's name, phone number and address will be printed. If the contact is not in the phonebook, the program will display an error.

### Search for a contact (by number)
To search a contact by the contact's number, press 4 and then enter. You will then have to input the number for the contact you would like to search for. The contact's name, phone number and address will be printed. If the contact is not in the phonebook, the program will display an error.

### Printing the phonebook
To print the entire phonebook, press 5 and then enter. All of the contacts, with their name, phone number and address, will be printed.

### Exiting the program
To exit the program, press 6 and then enter.

## Test cases for both Python and C
### Adding Contacts
Press 1 and then enter. Enter the following name, address and phone number:
```
Enter a name: James Smith
Enter a phone number: 12345678
Enter an address: 132 Main St

James Smith added successfully.
```

Press 5 and hit enter. The program should display the contact.
```
Name: James Smith, Address: 132 Main St, Phone Number: 12345678
```

Press 1 and then enter. Enter the following name:
```
Enter a name: James Smith
A contact with that name already exists.
```

Press 1 and then enter. Enter the following name, address and phone number:
```
Enter a name: James Connolly
Enter a phone number: 87654321
Enter an address: 931 Main St

James Connolly added successfully.
```
Press 5 and hit enter. The program should display the contact.
```
Name: James Smith, Address: 132 Main St, Phone Number: 12345678
Name: James Connolly, Address: 931 Main St, Phone Number: 87654321
```

Press 1 and then enter. Enter the following name and number:
```
Enter a name: Arthur Smith
Enter a phone number: 12345678
A contact with that number already exists.
```

### Deleting Contacts
Make sure the first contact from *Adding Contacts* is added first.  
Press 2 and then enter. Enter the following name:
```
Enter a name to delete: James Smith

James Smith deleted successfully
```
Press 5 and hit enter. The program should no longer display the contact.
```
Name: James Connolly, Address: 931 Main St, Phone Number: 87654321
```

### Searching for contact by name
Make sure the second contact from *Adding Contacts* is added first.  
Press 3 and then enter. Enter the following name:
```
Enter name to search for: James Connolly
```
The program should display the following
```
Name: James Connolly
Address: 931 Main St
Phone number: 87654321
```

Press 3 and then enter. Enter the following name:
```
Enter name to search for: Arthur Smith
```
The program should display the following
```
Contact not found
```

### Searching for contact by number
Make sure the second contact from *Adding Contacts* is added first.  
Press 4 and then enter. Enter the following name:
```
Enter number to search for: 87654321
```
The program should display the following
```
Name: James Connolly
Address: 931 Main St
Phone number: 87654321
```

Press 4 and then enter. Enter the following name:
```
Enter name to search for: Arthur Smith
```
The program should display the following
```
Contact not found
```

### Printing the phonebook
Make sure the second contact from *Adding Contacts* is added first.  
Add the first contact from *Adding Contacts* back into the phonebook.  
Press 1 and then enter. Enter the following name, address and phone number:
```
Enter a name: James Smith
Enter a phone number: 12345678
Enter an address: 132 Main St

James Smith added successfully.
```
Press 5 and hit enter. The program should display the contact.
```
Name: James Connolly, Address: 931 Main St, Phone Number: 87654321
Name: James Smith, Address: 132 Main St, Phone Number: 12345678
```
To demonstrate that the phonebook is not saved between launches of the program, close the program by pressing 6 and hitting enter.  
Re-execute the program. Then press 5 and hit enter. The program should not print anything as there are no entries in the phonebook.

### Exiting the program
Press 6 and hit enter.  
The program should close automatically.