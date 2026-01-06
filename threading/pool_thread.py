import time
from concurrent.futures.thread import ThreadPoolExecutor
import threading

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
        self.account_lock = threading.Lock()

    def withdraw(self, amount):
        with self.account_lock:
            if self.balance >= amount:
                new_balance = self.balance - amount
                print(f"Withdrawing {amount}")
                time.sleep(0.1)
                self.balance = new_balance

    def deposit(self, amount):
        with self.account_lock:
            new_balance = self.balance + amount
            print(f"Depositing {amount}")
            time.sleep(0.1)
            self.balance = new_balance




account = BankAccount(balance=1000)

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(account.withdraw, 700)
    executor.submit(account.deposit, 1000)
    executor.submit(account.withdraw, 300)

