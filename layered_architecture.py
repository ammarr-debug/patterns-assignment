

class AccountRepository:
    def __init__(self):
        # Simulated database table
        self._data = {
            1: {"name": "Alice", "balance": 100.0},
            2: {"name": "Bob", "balance": 30.0}
        }

    def get_account(self, user_id: int):
        return self._data.get(user_id)

    def update_balance(self, user_id: int, new_balance: float):
        if user_id in self._data:
            self._data[user_id]["balance"] = new_balance
            return True
        return False

class BankingService:
    def __init__(self, repo: AccountRepository):
        self.repo = repo

    def transfer(self, sender_id: int, receiver_id: int, amount: float):
        if amount <= 0:
            return False, "Amount must be greater than zero."

        sender = self.repo.get_account(sender_id)
        receiver = self.repo.get_account(receiver_id)

        if not sender or not receiver:
            return False, "One of the accounts does not exist."

        if sender["balance"] < amount:
            return False, f"Insufficient funds! You only have ${sender['balance']:.2f}"

        # Execute balance update
        self.repo.update_balance(sender_id, sender["balance"] - amount)
        self.repo.update_balance(receiver_id, receiver["balance"] + amount)
        return True, "Transfer completed successfully!"

class BankingCLI:
    def __init__(self, service: BankingService):
        self.service = service

    def send_money(self, sender_id: int, receiver_id: int, amount: float):
        print(f"\n[CLI] Attempting to transfer ${amount:.2f} from User {sender_id} to User {receiver_id}...")
        success, message = self.service.transfer(sender_id, receiver_id, amount)
        if success:
            print(f"[CLI Output] SUCCESS: {message}")
        else:
            print(f"[CLI Output] ERROR: {message}")


if __name__ == "__main__":
    repo = AccountRepository()
    service = BankingService(repo)
    cli = BankingCLI(service)


    cli.send_money(sender_id=1, receiver_id=2, amount=40.0)

    cli.send_money(sender_id=2, receiver_id=1, amount=200.0)