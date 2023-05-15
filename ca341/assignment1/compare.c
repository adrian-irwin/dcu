#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STRING_SIZE 100

struct phonebookEntry {
    char name[MAX_STRING_SIZE];
    char address[MAX_STRING_SIZE];
    int number;
    struct phonebookEntry * left;
    struct phonebookEntry * right;
};
typedef struct phonebookEntry phonebookEntry;

phonebookEntry * createEntry(char * name, char * address, int number);
phonebookEntry * insertEntry(phonebookEntry * root, char * name, char * address, int number, char * sortType);
phonebookEntry * searchEntry(phonebookEntry * root, char * name, int number);
phonebookEntry * deleteEntry(phonebookEntry * root, char * name, int number);
void printPhonebook(phonebookEntry * root);
void userPrompt(phonebookEntry * root, phonebookEntry * numberRoot);
int getNumberInput();
int getUserChoice();

int main(){
    phonebookEntry * root = NULL;
    phonebookEntry * numberRoot = NULL;

    printf("Welcome to your phonebook!\n\n");

    userPrompt(root, numberRoot);

    return 0;
}

// Creates a new phonebook entry and returns it
phonebookEntry * createEntry(char * name, char * address, int number) {
    // Allocate memory for the new entry and then copy the values into it
    phonebookEntry * newEntry = malloc(sizeof(phonebookEntry));
    strcpy(newEntry->name, name);
    strcpy(newEntry->address, address);
    newEntry->number = number;
    newEntry->left = NULL;
    newEntry->right = NULL;
    return newEntry;
}

// Inserts a new entry into the phonebook, that is sorted by name or number, in its correct position
phonebookEntry * insertEntry(phonebookEntry * root, char * name, char * address, int number, char * sortType) {

    // If the root is null, then we have reached the end of the phonebook and can insert the new entry here
    if (root == NULL) {
        return createEntry(name, address, number);
    }

    if (strcmp(sortType, "name") == 0) {
    // If the name is less than the root's name, then we need to insert the new entry to the left
    // otherwise we need to insert it to the right
        if (strcmp(name, root->name) < 0) {
            root->left = insertEntry(root->left, name, address, number, "name");
        }
        else if (strcmp(name, root->name) > 0) {
            root->right = insertEntry(root->right, name, address, number, "name");
        }
    }
    else if (strcmp(sortType, "number") == 0) {
    // If the number is less than the root's name, then we need to insert the new entry to the left
    // otherwise we need to insert it to the right
        if (number < root->number) {
            root->left = insertEntry(root->left, name, address, number, "number");
        }
        else if (number > root->number) {
            root->right = insertEntry(root->right, name, address, number, "number");
        }
    }

    return root;
}

// Searches for a given name or number in the phonebook, and returns the entry if found
phonebookEntry * searchEntry(phonebookEntry * root, char * name, int number) {
    // If the root is null, then we have reached the end of the phonebook and the entry was not found
    if (root == NULL) {
        return NULL;
    }
    if (strcmp(name, "") != 0) {
        // If the name is less than the root's name, then we need to search the left subtree
        // If the name is greater than the root's name, then we need to search the right subtree
        // Otherwise we have found the entry and can return it
        if (strcmp(name, root->name) < 0) {
            return searchEntry(root->left, name, 0);
        }
        else if (strcmp(name, root->name) > 0) {
            return searchEntry(root->right, name, 0);
        }
        else {
            return root;
        }
    }
    else if (number != 0) {
        // If the number is less than the root's number, then we need to search the left subtree
        // If the number is greater than the root's number, then we need to search the right subtree
        // Otherwise we have found the entry and can return it
        if (number < root->number) {
            return searchEntry(root->left, "", number);
        }
        else if (number > root->number) {
            return searchEntry(root->right, "", number);
        }
        else {
            return root;
        }
    }

}

// Deletes a given entry from the phonebook, that is sorted by name or number, and returns the new root
// https://www.geeksforgeeks.org/deletion-in-binary-search-tree/
phonebookEntry * deleteEntry(phonebookEntry * root, char * name, int number) {
    // If the root is null, then we have reached the end of the phonebook and the entry was not found and could not be deleted
    if (root == NULL) {
        return NULL;
    }

    // In both cases, we need to search for the entry to be deleted, if the value is less than the root's value, then we need to search the left subtree, otherwise we need to search the right subtree, if we find the entry, then we can delete it

    if (strcmp(name, "") != 0) {
        // If the name is less than the root's name, then the left subtree will be searched for the entry
        if (strcmp(name, root->name) < 0) {
            root->left = deleteEntry(root->left, name, 0);
        }
        // If the name is greater than the root's name, then the right subtree will be searched for the entry
        else if (strcmp(name, root->name) > 0) {
            root->right = deleteEntry(root->right, name, 0);
        }
        // If the name is equal to the root's name, then this is the entry to be deleted
        else {
            if (root->left == NULL) {
                phonebookEntry * temp = root->right; // Store the subtree in a temporary variable
                free(root); // Free the memory used by the root
                return temp; // Return the subtree as the new root
            }
            else if (root->right == NULL) {
                phonebookEntry * temp = root->left;
                free(root);
                return temp;
            }

            // If the root has two children, then the right subtree must be searched for the smallest entry
            phonebookEntry * temp = root->right; // Store the right subtree in a temporary variable
            // Loop down the left subtree to find the smallest entry
            // The final value of temp will be the smallest entry in the right subtree and will replace the root
            while (temp->left != NULL) {
                temp = temp->left;
            }
            strcpy(root->name, temp->name);
            strcpy(root->address, temp->address);
            root->number = temp->number;
            // To not have a duplicate entry in the phonebook, the smallest entry in the right subtree is deleted
            root->right = deleteEntry(root->right, temp->name, 0);
        }
    }
    else if (number != 0) {
        if (number < root->number) {
            root->left = deleteEntry(root->left, "", number);
        }
        else if (number > root->number) {
            root->right = deleteEntry(root->right, "", number);
        }
        else {
            if (root->left == NULL) {
                phonebookEntry * temp = root->right;
                free(root);
                return temp;
            }
            else if (root->right == NULL) {
                phonebookEntry * temp = root->left;
                free(root);
                return temp;
            }

            phonebookEntry * temp = root->right;
            while (temp->left != NULL) {
                temp = temp->left;
            }
            strcpy(root->name, temp->name);
            strcpy(root->address, temp->address);
            root->number = temp->number;
            root->right = deleteEntry(root->right, "", temp->number);
        }
    }
    return root;
}

// Prints the phonebook in alphabetical order
void printPhonebook(phonebookEntry * root) {
    // First the left subtree is printed, then the root, then the right subtree
    if (root == NULL) {
        return;
    }
    printPhonebook(root->left);
    printf("Name: %s, Address: %s, Phone Number: %d\n", root->name, root->address, root->number);
    printPhonebook(root->right);
}

// Gets the user's input and parses it to an integer
int getNumberInput() {
    int number;
    char input[MAX_STRING_SIZE];
    fgets(input, MAX_STRING_SIZE, stdin);

    // https://stackoverflow.com/a/1248017 - Remove newline character at the end of the string and replace it with a null terminator
    if ((strlen(input) > 0) && (input[strlen(input) - 1] == '\n')) {
        input[strlen (input) - 1] = '\0';
    }

    // strtol is used to convert string to int
    number = strtol(input, NULL, 10);
    if (number < 1) {
        printf("Invalid input.\nInput can only be positive, less than 11 digits long and no larger than 2147483647\nEnter number: ");
        return getNumberInput();
    }

    return number;
}

// Prompts the user for a choice and returns it
int getUserChoice() {
    int choice;
    printf("\n");
    printf("1. Add a new contact\n");
    printf("2. Delete a contact\n");
    printf("3. Search for a contact (by name)\n");
    printf("4. Search for a contact (by number)\n");
    printf("5. Print the phonebook\n");
    printf("6. Exit\n");
    printf("\nEnter a number: ");

    choice = getNumberInput();
    return choice;
}

// Takes the user's choice and performs the appropriate action
void userPrompt(phonebookEntry * root, phonebookEntry * numberRoot) {
    int choice = getUserChoice();
    printf("\n");
    char name[MAX_STRING_SIZE];
    char address[MAX_STRING_SIZE];
    int number;
    char input[MAX_STRING_SIZE];
    phonebookEntry * temp = malloc(sizeof(phonebookEntry));
    phonebookEntry * searchResult = malloc(sizeof(phonebookEntry));
    // Switch statement to perform the appropriate action based on the user's choice
    // Will loop until the user chooses to exit by inputting 6
    while (choice != 6) {
        switch (choice) {
            case 1:
                // Adding a new contact to the phonebook

                printf("Enter a name: ");
                fgets(name, MAX_STRING_SIZE, stdin);
                if ((strlen(name) > 0) && (name[strlen(name) - 1] == '\n')) {
                    name[strlen (name) - 1] = '\0';
                }
                // check if the name already exists in the phonebook
                searchResult = searchEntry(root, name, 0);
                if (searchResult != NULL) {
                    printf("A contact with that name already exists.\n");
                    break;
                }

                printf("Enter a phone number: ");
                number = getNumberInput();
                if (number == 0) {
                    printf("Invalid phone number entered. Please try again.\n");
                    break;
                }
                // check if the number already exists in the phonebook
                searchResult = searchEntry(numberRoot, "", number);
                if (searchResult != NULL) {
                    printf("A contact with that number already exists.\n");
                    break;
                }

                printf("Enter an address: ");
                fgets(address, MAX_STRING_SIZE, stdin);
                if ((strlen(address) > 0) && (address[strlen(address) - 1] == '\n')) {
                    address[strlen (address) - 1] = '\0';
                }

                root = insertEntry(root, name, address, number, "name");
                numberRoot = insertEntry(numberRoot, name, address, number, "number");

                printf("\n%s added successfully.\n", name);
                break;

            case 2:
                // Deleting a contact from the phonebook

                printf("Enter a name to delete: ");
                fgets(name, MAX_STRING_SIZE, stdin);
                if ((strlen(name) > 0) && (name[strlen(name) - 1] == '\n')) {
                    name[strlen (name) - 1] = '\0';
                }

                // The entry needs to be deleted from both the name and number sorted phonebooks
                // To be found in the number sorted phonebook, the number needs to be found first from the name sorted phonebook
                temp = searchEntry(root, name, 0);
                if (temp == NULL) {
                    printf("Contact not found.\n");
                    break;
                }
                int tempNumber = temp->number;
                root = deleteEntry(root, name, 0);
                numberRoot = deleteEntry(numberRoot, "", tempNumber);
                printf("\n%s deleted successfully\n", name);
                temp = NULL;
                break;

            case 3:
                // Searching for a contact by name

                printf("Enter name to search for: ");
                fgets(name, MAX_STRING_SIZE, stdin);
                if ((strlen(name) > 0) && (name[strlen(name) - 1] == '\n')) {
                    name[strlen (name) - 1] = '\0';
                }

                phonebookEntry * searchResult = searchEntry(root, name, 0);
                if (searchResult != NULL) {
                    printf("Name: %s\n", searchResult->name);
                    printf("Address: %s\n", searchResult->address);
                    printf("Phone number: %d\n", searchResult->number);
                }
                else {
                    printf("Contact not found\n");
                }
                break;

            case 4:
                // Searching for a contact by number

                printf("Enter number to search for: ");
                number = getNumberInput();
                phonebookEntry * searchNumberResult = searchEntry(numberRoot, "", number);
                if (searchNumberResult != NULL) {
                    printf("Name: %s\n", searchNumberResult->name);
                    printf("Address: %s\n", searchNumberResult->address);
                    printf("Phone number: %d\n", searchNumberResult->number);
                }
                else {
                    printf("Contact not found\n");
                }
                break;

                case 5:
                    // Printing the phonebook
                    printPhonebook(root);
                    break;

            default:
                printf("Please enter a valid option\n\n");
                break;
        }
        choice = getUserChoice();
        printf("\n");
    }
    free(temp);
}