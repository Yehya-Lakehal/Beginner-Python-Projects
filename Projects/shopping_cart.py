# Shopping Cart

purchases = []
print("Welcome to Your Shopping Cart! I hope that you get a nice shopping <3")

def get_purchases():
    if purchases:
        print("Shopping Cart:")
        for i in purchases:
            print(f"   {purchases.index(i)+1}- {i}.")
    else:
        print("Shopping Cart is Empty!")

while True:
    command = input("> ").lower()
    
    if command == "q":
        print("Thank you for using our shopping cart! Bye <3")
        break
    elif "buy " in command:
        purchases.append(command[command.index(" ")+1:])
        continue
    elif "remove " in command:
        purchases.remove(command[command.index(" ")+1:])
        continue
    elif command == "show":
        get_purchases()
        break
    elif command == "help" or command == "h":
        print(
"""Help: - type \'buy [something]\' to add items to cart.
      - type \'remove [something]\' to remove items from cart.
      - type \'q\' to quit!""")
    else:
        print("Error: Invalid command! type 'h' for help!")
