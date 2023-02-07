class ShoppingCart:
    items: list[str] = []
    prices: list[float] = []

    def addItem(shoppingCart, item: str, price: float):
        return shoppingCart.addItems([item], [price])

    def addItems(shoppingCart, items: list[str], prices: list[float]) -> str:
        if len(items) != len(prices):
            return "ERROR: The length of items and prices must be equal"

        shoppingCart.items.extend(items)
        shoppingCart.prices.extend(prices)

        return "SUCCESS"

    def removeItems(shoppingCart, indexes: list[int]) -> str:
        for index in indexes:
            if index >= len(shoppingCart.items):
                return "ERROR: One or more indexes are not present in the shopping cart"
        
        for index in indexes:
            del shoppingCart.items[index]
            del shoppingCart.prices[index]

        return "SUCCESS"
    
    def totalPrice(shoppingCart) -> float:
        totalPrice: float = 0

        for price in shoppingCart.prices:
            totalPrice += price

        return totalPrice

    def clearCart(shoppingCart) -> str:
        shoppingCart.items.clear()
        shoppingCart.prices.clear()

def prompt():
    print("""
    
    -------------------------------------------------------------------

    A - Add item(s) to the cart
    R - Remove item(s) from the cart
    V - View all items in the cart
    T - Get the total price of all items in the cart
    C - Clear the cart
    Q - Quit the program

    Enter the character associated with the action you wish to perform:
    """)

    userPrompt = input("> ")

    if userPrompt == "A":
        promptA()
    elif userPrompt == "R":
        promptR()
    elif userPrompt == "V":
        promptV()
    elif userPrompt == "T":
        print("""

        Cart total: """ + str(shoppingCart.totalPrice()) + """
        """)
        
        prompt()
        return
    elif userPrompt == "C":
        print("""

        List cleared.
        """)

        shoppingCart.clearCart()
        
        prompt()
        return
    elif userPrompt == "Q":
        print("""

        Quitting the program...
        """)

        return
    else:
        print("""

        Unrecognized action. Please try again.
        """)

        prompt()
        return 
    
def promptA():
    counter = 1
    going = True

    items: list[str] = []
    prices: list[float] = []

    while going:
        print("""
        
        Enter the name of item #""" + str(counter) + """ (or leave it blank if you are finished adding items): 
        """)

        name = input("> ")

        if name == "":
            going = False
            continue

        print("""
        
        Enter the price of item #""" + str(counter) + """: 
        """)

        price = input("> ")

        try:
            priceFloat = float(price)
        except:
            print("""

            Please enter a valid price (eg. 3.26). Try again.
            """)
            continue

        items.append(name)
        prices.append(priceFloat)

        counter += 1

    shoppingCart.addItems(items, prices)

    prompt()

    return

def promptR():
    counter = 1
    toRemove: list[int] = []
    print("""

    """)
    for item in shoppingCart.items:
        print("(" + str(counter) + "): " + item)
        counter += 1

    print("""
    Enter the number(s) corresponding to the item(s) you wish to remove from the cart:
    """)

    numbersInput = input()

    numbers = numbersInput.split(",")

    for number in numbers:
        try:
            intNumber = int(number)
        except:
            print("""
            One or more of your inputs is not a valid number. Please try again.
            """)

            prompt()
            return
        
        toRemove.append(intNumber - 1)

    shoppingCart.removeItems(toRemove)

    prompt()
    return

def promptV():
    if len(shoppingCart.items) == 0:
        print("""

        Shopping cart is empty
        """)

        prompt()
        return

    counter = 1
    print("""

    """)
    for item in shoppingCart.items:
        print("(" + str(counter) + "): NAME: " + item + " PRICE: " + str(shoppingCart.prices[counter - 1]))
        counter += 1

    prompt()
    return

if __name__ == "__main__":
    shoppingCart = ShoppingCart()
    prompt()

print(shoppingCart.items)