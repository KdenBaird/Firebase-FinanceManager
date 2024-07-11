import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the service account
# Loads the credentials from the JSON file and finds the account key
cred = credentials.Certificate("C:/Users/Caden Baird/OneDrive/Desktop/Programming Courses/Applied Programming/Sprint #4 Cloud Database/sprint-4-66a56-firebase-adminsdk-aim6r-19cc867fe8.json")

# Initializes firebase app with the credentials saved
firebase_admin.initialize_app(cred)

# Creates a client to interact with the database
db = firestore.client()

# Using key-value pairs for the db in all the functions
def add_income():
    source = input("Source: ")
    amount = float(input("Amount: "))
    date = input("Date (YYYY-MM-DD): ")
    doc_id = db.collection('Incomes').add({
        'source': source,
        'amount': amount,
        'date': date
    })

def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))
    date = input("Date (YYYY-MM-DD): ")
    doc_ref, doc_id = db.collection('Expenses').add({
        'category': category,
        'amount': amount,
        'date': date
    })
    


# .stream and income.to_dict basically converts it to a dictionary to print or read
def view_incomes():
    incomes = db.collection('Incomes').stream()
    for income in incomes:
        print(f"Document ID: {income.id}, Data: {income.to_dict()}")
    return "Displayed incomes.\n"

def view_expenses():
    expenses = db.collection('Expenses').stream()
    for expense in expenses:
        print(f"Document ID: {expense.id}, Data: {expense.to_dict()}")
    return "Displayed expenses.\n"

def delete_income_or_expense():
    collection = input("Which collection would you like to delete from (Incomes/Expenses)? ")
    
    # Loop until a valid collection name is entered
    while collection.lower() not in ['incomes', 'expenses']:
        print("Invalid collection. Please enter 'Incomes' or 'Expenses'.")
        collection = input("Which collection would you like to delete from (Incomes/Expenses)?\n ")

    # Get all documents in the specified collection
    documents = db.collection(collection.capitalize()).stream()
    
    # Display document IDs along with their information
    print(f"Document IDs and Information in {collection.capitalize()} collection:")
    for doc in documents:
        print(f"Document ID: {doc.id}")
        print(f"Data: {doc.to_dict()}")
        print("---------------------------------")

    # Loop until a valid document ID is entered
    while True:
        document_id = input("Enter the document ID to delete: ")
        doc_ref = db.collection(collection.capitalize()).document(document_id).get()
        
        if doc_ref.exists:
            # If the document exists, delete it and return success message
            db.collection(collection.capitalize()).document(document_id).delete()
            return f"Document with ID {document_id} deleted from {collection.capitalize()} collection."
        else:
            # If the document does not exist, prompt the user to enter a valid document ID
            print("Invalid document ID. Please enter a valid document ID.")

def default_case():
    return "Invalid choice. Please try again."

def main_menu():
    while True:
        print("Personal Finance Manager")
        print("1. Add Income or Expense")
        print("2. View Incomes")
        print("3. View Expenses")
        print("4. Delete Income or Expense")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            response = input("Would you like to add income (1) or add expenses (2)? ")
            if response == "1":
                add_income()
                print("Income Added. \n")
            elif response == "2":
                add_expense()
                print("Expense Added. \n")
            else:
                print("Invalid input. Please enter 1 or 2.")
        elif choice == "2":
            print(view_incomes())
        elif choice == "3":
            print(view_expenses())
        elif choice == "4":
            print(delete_income_or_expense())
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print(default_case())

if __name__ == "__main__":
    main_menu()
