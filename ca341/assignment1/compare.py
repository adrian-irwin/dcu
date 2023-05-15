class phonebookEntry:
    def __init__(self, name, number, address):
        """Constructor for phonebookEntry class

        Args:
            name (string): name for the phonebook entry
            number (integer): number for the phonebook entry
            address (string): address for the phonebook entry
        """
        self.left = None
        self.right = None
        self.name = name
        self.number = number
        self.address = address

    def insert(self, name, number, address, sortType="name"):
        """Inserts a new phonebook entry into the phonebook, sorted by either name or number

        Args:
            name (string): name to insert into the phonebook
            number (integer): number to insert into the phonebook
            address (string): address to insert into the phonebook
            sortType (string, optional): The type of sorting to use. Defaults to "name".
        """
        if sortType == "name":
            compareOn = self.name
            compareWith = name
        elif sortType == "number":
            compareOn = self.number
            compareWith = number

        if compareOn:
            if compareWith < compareOn:
                if self.left is None:
                    self.left = phonebookEntry(name, number, address)
                else:
                    self.left.insert(name, number, address, sortType)
            elif compareWith > compareOn:
                if self.right is None:
                    self.right = phonebookEntry(name, number, address)
                else:
                    self.right.insert(name, number, address, sortType)

    def printPhonebook(self):
        """Prints the phonebook"""
        if self.left:
            self.left.printPhonebook()
        print(f"Name: {self.name}, Phone Number: {self.number}, Address: {self.address}")
        if self.right:
            self.right.printPhonebook()

    def search(self, searchFor, sortType="name"):
        """Searches for either a name and number in the phonebook and returns the full entry

        Args:
            searchFor (string): name or number to search for in the phonebook
            sortType (string, optional): The type of sorting to use. Defaults to "name".
        Returns:
            phonebookEntry: The phonebook entry with the name or the number searched for is in
        """
        if sortType == "name":
            compareOn = self.name
        elif sortType == "number":
            compareOn = self.number


        if searchFor < compareOn and self.left is not None:
            return self.left.search(searchFor, sortType)
        elif searchFor > compareOn and self.right is not None:
            return self.right.search(searchFor, sortType)
        elif searchFor == compareOn:
            return self
        else:
            return None

    def findMin(self):
        """Finds the minimum value in the given phonebook
            Used as a utility function for the delete functions

        Returns:
            list: A list containing the name and number of the minimum value
        """
        if self.left is None:
            return self
        else:
            return self.left.findMin()

    def delete(self, deleteItem, sortType="name"):
        """Deletes an entry from the phonebook based on either the name or the number

        Args:
            deleteItem (string): name or number to delete from the phonebook
            sortType (str, optional): The type of sorting to use. Defaults to "name".

        Returns:
            phonebookEntry: The phonebook with the entry deleted
        """
        if sortType == "name":
            compareOn = self.name
        elif sortType == "number":
            compareOn = self.number

        if deleteItem == usrName or deleteItem == usrNumber:
            return
        if deleteItem < compareOn:
            if self.left:
                self.left = self.left.delete(deleteItem, sortType)
        elif deleteItem > compareOn:
            if self.right:
                self.right = self.right.delete(deleteItem, sortType)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            middleVal = self.right.findMin()
            self.name = middleVal.name
            self.number = middleVal.number
            self.address = middleVal.address
            if sortType == "name":
                self.right = self.right.delete(middleVal.name, sortType)
            elif sortType == "number":
                self.right = self.right.delete(middleVal.number, sortType)
        return self

def validateNumber(number):
    """Utility function to validate the number entered by the user

    Args:
        number (string): number entered by the user

    Returns:
        integer: The number entered by the user covnerted to an integer
    """
    while True:
        try:
            number = int(number)
            break
        except ValueError:
            print("Invalid number. Please try again.")
            number = input("Enter the number again: ")
    return number

def getUserChoice():
    """Prompts the user for input

    Returns:
        integer: The user's choice
    """
    print()
    print("1. Add a new contact")
    print("2. Delete a contact")
    print("3. Search for a contact (by name)")
    print("4. Search for a contact (by number)")
    print("5. Print all contacts")
    print("6. Exit")
    print()
    userInput = validateNumber(int(input("Enter a number: ")))
    print()
    return userInput

def userPrompt():
    """Prompts the user for input and calls the appropriate function based on the user's choice"""
    userChoice = getUserChoice()
    try:
        while userChoice != 6:
            if userChoice == 1:
                # add a new contact
                name = input("Enter a name: ")
                if root.search(name, "name") is not None:
                    print("Name already exists in the phonebook")
                    userChoice = getUserChoice()
                    continue

                number = validateNumber(int(input("Enter a phone number: ")))
                if numberRoot.search(number, "number") is not None:
                    print("Name already exists in the phonebook")
                    userChoice = getUserChoice()
                    continue
                address = input("Enter an address: ")

                root.insert(name, number, address, "name")
                numberRoot.insert(name, number, address, "number")

                print(f"\n{name} added successfully.")
                userChoice = int(getUserChoice())

            elif userChoice == 2:
                # delete a contact
                nameToDelete = input("Enter a name to delete: ")
                delete = root.search(nameToDelete, "name")
                if delete is None:
                    print("Contact not found.")

                elif delete.name == usrName:
                    print("You can't delete yourself!")
                else:
                    numberToDelete = delete.number

                    root.delete(nameToDelete, "name")
                    numberRoot.delete(numberToDelete, "number")

                    print(f"\n{name} deleted successfully.")
                userChoice = int(getUserChoice())

            elif userChoice == 3:
                # search for a contact by name
                search = input("Enter name to search for: ")
                searchResult = root.search(search, "name")

                if searchResult is not None:
                    print(f"Name: {searchResult.name}\nNumber: {searchResult.number}\nAddress: {searchResult.address}")
                else:
                    print(f"{search} Not Found")

                userChoice = int(getUserChoice())

            elif userChoice == 4:
                # search for a contact by number
                search = validateNumber(int(input("Enter number to search for: ")))
                searchResult = numberRoot.search(search, "number")

                if searchResult is not None:
                    print(f"Name: {searchResult.name}\nNumber: {searchResult.number}\nAddress: {searchResult.address}")
                else:
                    print(f"{search} Not Found")

                userChoice = int(getUserChoice())

            elif userChoice == 5:
                # print all contacts
                root.printPhonebook()
                userChoice = int(getUserChoice())

            else:
                # invalid input
                print("\nInvalid input\n")
                userChoice = int(getUserChoice())

    # if the user enters a non-integer value for the menu choice this will catch it and prompt the user to try again
    except ValueError:
        print("Invalid input")
        userPrompt()


usrName = input("Enter your name: ")
usrNumber = validateNumber(int(input("Enter your number: ")))
usrAddress = input("Enter your address: ")
root = phonebookEntry(usrName, usrNumber, usrAddress)
numberRoot = phonebookEntry(usrName, usrNumber, usrAddress)


def main():
    print(f"Welcome your phonebook, {usrName}!")

    userPrompt()

if __name__ == "__main__":
    main()