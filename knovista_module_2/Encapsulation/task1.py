class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        # Initialize through the setter to ensure validation rules run on creation
        self.balance = initial_balance

    # --- GETTER ---
    @property
    def balance(self) -> float:
        """The balance property getter."""
        return self.__balance

    # --- SETTER ---
    @balance.setter
    def balance(self, amount: float):
        """The balance property setter with validation."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Balance must be a number.")
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        
        self.__balance = float(amount)


# --- Example Usage ---
account = BankAccount("Priya", 5000.0)

# 1. Access balance like a standard attribute (invokes @property getter)
print(f"Owner: {account.owner}, Balance: ₹{account.balance}")

# 2. Modify balance cleanly (invokes @balance.setter)
account.balance = 7500.0
print(f"Updated Balance: ₹{account.balance}")

# 3. Trying to assign invalid values triggers validation errors:
try:
    account.balance = -1500  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

try:
    account.balance = "invalid_amount"  # Raises TypeError
except TypeError as e:
    print(f"Error: {e}")

# 4. Direct private access fails due to name mangling
try:
    print(account.__balance)
except AttributeError as e:
    print(f"Blocked private access: {e}")