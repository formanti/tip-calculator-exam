import csv
from datetime import datetime

def get_bill_amount():
    while True:
        try:
            amount = float(input("Enter bill amount: $"))
            if amount <= 0:
                print("Error: Amount must be positive!")
                continue
            return amount
        except ValueError:
            print("Error: Please enter a valid number!")

def calculate_tip():
    print("\n=== Calculate Tip ===")
    bill = get_bill_amount()
    
    print("Tip Options: 1) 15%  2) 18%  3) 20%  4) 25%")
    choice = input("Choose (1-4): ")
    
    tip_rates = {"1": 15, "2": 18, "3": 20, "4": 25}
    tip_percent = tip_rates.get(choice, 20)
    
    tip = bill * (tip_percent / 100)
    total = bill + tip
    
    print(f"Bill: ${bill:.2f}")
    print(f"Tip ({tip_percent}%): ${tip:.2f}")
    print(f"Total: ${total:.2f}")
    
    # NEW: Save to CSV
    try:
        with open('tip_history.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            date = datetime.now().strftime("%Y-%m-%d %H:%M")
            writer.writerow([date, bill, tip_percent, tip, total])
        print("✅ Saved to history!")
    except Exception as e:
        print(f"Error saving: {e}")

def view_history():
    print("\n=== CALCULATION HISTORY ===")
    try:
        with open('tip_history.csv', 'r') as file:
            reader = csv.reader(file)
            calculations = list(reader)
        
        if not calculations:
            print("No calculations yet!")
            return
            
        for calc in calculations:
            date, bill, tip_percent, tip_amount, total = calc
            print(f"{date} | Bill: ${bill} | Tip: {tip_percent}% (${tip_amount}) | Total: ${total}")
            
    except FileNotFoundError:
        print("No history found!")

def main():
    print("💰 Tip Calculator")
    
    while True:
        print("\n1. Calculate tip  2. View history  3. Exit")
        choice = input("Choose: ")
        
        if choice == "1":
            calculate_tip()
        elif choice == "2":
            view_history()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Choose 1, 2, or 3!")

if __name__ == "__main__":
    main()