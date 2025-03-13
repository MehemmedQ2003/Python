import json
from datetime import datetime

FILE_NAME = "data.json"

# todo Load Data from JSON file
def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# todo Save Data to JSON file
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


# todo Add record to database
def add_record():
    try:
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        description = input("Enter a short description: ")
        date = input("Enter the date: ")

        datetime.strptime(date, "%Y-%m-%d")

        records = load_data()
        records.append({"amount": amount, "category": category, "description": description, "date": date})
        save_data(records)
        print("Record added!")
    except ValueError as e:
        print(e)


# todo Show records
def show_records():
    records = load_data()
    if not records:
        print("There are no records to show.")
        return

    else:
        for record in records:
            print(f"{record['date']} - {record['category']} - {record['amount']} USD - {record['description']}")


# todo Calculate summary
def view_summary():
    records = load_data()
    
    sum_income = 0
    for r in records:
        if(r['amount'] > 0):
            sum_income += r['amount']

    sum_expenses = 0
    for r in records:
        if(r['amount'] < 0):
            sum_expenses += abs(r['amount'])

    print(f"Total Income: {sum_income} USD")
    print(f"Total Expenses: {sum_expenses} USD")
    print(f"Balance: {sum_income - sum_expenses} USD")


# todo Main function
def main():
    while True:
        print("\n1. Add a new record")
        print("2. Show records")
        print("3. View summary")
        print("4. Exit \n")

        choice = input("Make a selection: ")
        
        if choice == "1":
            add_record()
        elif choice == "2":
            show_records()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid selection! Please try again.")

if __name__ == "__main__":
    main()