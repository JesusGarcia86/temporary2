class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
   
    def make_deposit(self, amount):	
    	self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
sofia = User("Sofia Kenin", "skenin@python.com")
elina = User("Elina Svitolina", "esvitolina@python.com")
maria = User("Maria Sharapova", "msharapova@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(50)
guido.make_withdrawal(200)
guido.display_user_balance()

monty.make_deposit(100)
monty.make_deposit(100)
monty.make_withdrawal(25)
monty.make_withdrawal(150)	
#print(monty.account_balance)

sofia.make_deposit(500)
sofia.make_withdrawal(100)
sofia.make_withdrawal(50)
sofia.make_withdrawal(300)
#print(sofia.account_balance)

guido.transfer_money(elina, 100)
print(guido.account_balance)
print(elina.account_balance)
