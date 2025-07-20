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

def get_tip_percent():
    print("\nTip Options:")
    print("1. 15%")
    print("2. 18%") 
    print("3. 20%")
    print("4. 25%")
    print("5. Custom")
    
    while True:
        try:
            choice = input("Choose option (1-5): ")
            if choice == "1":
                return 15
            elif choice == "2":
                return 18
            elif choice == "3":
                return 20
            elif choice == "4":
                return 25
            elif choice == "5":
                custom = float(input("Enter custom tip %: "))
                if custom < 0:
                    print("Error: Tip cannot be negative!")
                    continue
                return custom
            else:
                print("Error: Choose 1-5!")
        except ValueError:
            print("Error: Invalid input!")

def calculate_and_save():
    bill = get_bill_amount()
    tip_percent = get_tip_percent()
    
    tip_amount = bill * (tip_percent / 100)
    total = bill + tip_amount
    
    print(f"\nBill: ${bill:.2f}")
    print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
    print(f"Total: ${total:.2f}")
    
    # Save to CSV
    try:
        with open('tip_history.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            date = datetime.now().strftime("%Y-%m-%d %H:%M")
            writer.writerow([date, bill, tip_percent, tip_amount, total])
        print("✅ Calculation saved!")
    except Exception as e:
        print(f"Error saving: {e}")

def view_history():
    try:
        with open('tip_history.csv', 'r') as file:
            reader = csv.reader(file)
            calculations = list(reader)
        
        if not calculations:
            print("No calculations yet!")
            return
            
        print("\n=== TIP CALCULATION HISTORY ===")
        for calc in calculations:
            date, bill, tip_percent, tip_amount, total = calc
            print(f"{date} | Bill: ${bill} | Tip: {tip_percent}% (${tip_amount}) | Total: ${total}")
            
    except FileNotFoundError:
        print("No history found. Calculate some tips first!")
    except Exception as e:
        print(f"Error reading history: {e}")

def main():
    print("💰 Advanced Tip Calculator")
    print("Features: Multiple tip options, history tracking, CSV persistence")
    
    while True:
        print("\n" + "="*40)
        print("1. Calculate tip")
        print("2. View calculation history")
        print("3. Exit")
        
        try:
            choice = input("\nChoose option (1-3): ").strip()
            
            if choice == "1":
                calculate_and_save()
            elif choice == "2":
                view_history()
            elif choice == "3":
                print("👋 Thanks for using the tip calculator!")
                break
            else:
                print("Error: Please choose 1, 2, or 3")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()