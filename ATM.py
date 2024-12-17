class ATM:
    def __init__(self, balance, atm_balance, withdrawal_limit, deposit_limit):
        self.balance = balance                 # User's account balance
        self.atm_balance = atm_balance         # Total cash in ATM
        self.withdrawal_limit = withdrawal_limit  # Maximum amount user can withdraw in a day
        self.deposit_limit = deposit_limit     # Maximum amount user can deposit in a single transaction
    
    def check_balance(self):
        return f"Your current balance is: ${self.balance}"

    def withdraw(self, amount):
        try:
            # Check if withdrawal amount exceeds the withdrawal limit
            if amount > self.withdrawal_limit:
                raise Exception(f"Error: You have exceeded the withdrawal limit of ${self.withdrawal_limit}")
            
            # Check if user has enough balance
            if amount > self.balance:
                raise Exception(f"Error: Insufficient balance. Your current balance is ${self.balance}")

            # Check if ATM has enough money
            if amount > self.atm_balance:
                raise Exception(f"Error: ATM is out of sufficient funds. Available in ATM: ${self.atm_balance}")
            
            # If all checks pass, process withdrawal
            self.balance -= amount
            self.atm_balance -= amount
            return f"Withdrawal successful! You withdrew ${amount}. Your remaining balance is ${self.balance}"

        except Exception as e:
            return str(e)  # Return the error message instead of crashing the program
    
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise Exception("Error: Deposit amount must be greater than zero.")
            
            # Check if the deposit exceeds the deposit limit
            if amount > self.deposit_limit:
                raise Exception(f"Error: Deposit amount exceeds the limit of ${self.deposit_limit}")
            
            # Deposit money to the user's balance and add it to the ATM balance
            self.balance += amount
            self.atm_balance += amount
            return f"Deposit successful! You deposited ${amount}. Your new balance is ${self.balance}."
        
        except Exception as e:
            return str(e)

def atm_menu():
    atm = ATM(balance=5000, atm_balance=10000, withdrawal_limit=3000, deposit_limit=2000)  # Set deposit limit
    
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            print(atm.check_balance())
        
        elif choice == '2':
            try:
                amount = int(input("Enter the amount to withdraw: "))
                print(atm.withdraw(amount))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif choice == '3':
            try:
                amount = int(input("Enter the amount to deposit: "))
                print(atm.deposit(amount))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif choice == '4':
            print("Exiting... Thank you for using the ATM.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    atm_menu()
