import sqlite3
import datetime
import pytz
# from decimal import *

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, account TEXT NOT NULL,"
            "amount INTEGER NOT NULL, PRIMARY KEY (time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS"
            " SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
            " history.account, history.amount FROM history ORDER BY history.time")

class Account(object):
    # _qb = Decimal('0.00')  # NOTE: class constant, accessible without creating an instance.

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())
        # This stores timezone info to database/server, but standard Python library can't
        # display them(need dateutil). So the checking script won't report any results.
        # local_time = pytz.utc.localize(datetime.datetime.utcnow())
        # return local_time.astimezone()

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
        # if row is not None:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            # self._balance = Decimal(opening_balance).quantize(Account._qb)
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float: # Decimal:
        # decimal_amount = Decimal(amount).quantize(Account._qb)
        # if decimal_amount > Account._qb:
        if amount > 0.0:
            # self._balance += amount
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float: # Decimal:
        # decimal_amount = Decimal(amount).quantize(Account._qb)
        # if Account._qb < decimal_amount <= self._balance:
        if 0 < amount <= self._balance:
            # self._balance -= amount
            # new_balance = self._balance - amount
            # withdrawal_time = Account._current_time()
            # db.execute("UPDATE acounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES (?, ?, ?)", (withdrawal_time, self.name, -amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
            # return decimal_amount
            return amount / 100
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return 0.0  # Account._qb

    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))


if __name__ == '__main__':
    tim = Account("Tim")
    tim.deposit(1010)
    tim.deposit(10)
    tim.deposit(10)
    tim.withdraw(30)
    tim.withdraw(0)
    tim.show_balance()

    terry = Account("Terry")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    terryG = Account("TerryG")
    michael = Account("Michael")

    db.close()
