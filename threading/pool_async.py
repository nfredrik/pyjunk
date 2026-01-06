import asyncio

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.account_lock = asyncio.Lock()

    async def withdraw(self, amount):
        async with self.account_lock:
            if self.balance >= amount:
                new_balance = self.balance - amount
                print(f"Withdrawing {amount}")
                await asyncio.sleep(0.1)  # Simulate I/O operation
                self.balance = new_balance
                print(f"New balance after withdrawal: {self.balance}")

    async def deposit(self, amount):
        async with self.account_lock:
            new_balance = self.balance + amount
            print(f"Depositing {amount}")
            await asyncio.sleep(0.1)  # Simulate I/O operation
            self.balance = new_balance
            print(f"New balance after deposit: {self.balance}")

async def main():
    account = BankAccount(balance=1000)
    
    # Run operations concurrently
    await asyncio.gather(
        account.withdraw(700),
        account.deposit(1000),
        account.withdraw(300)
    )
    
    print(f"Final balance: {account.balance}")

if __name__ == "__main__":
    asyncio.run(main())
