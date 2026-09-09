
# ------------- # -- Mini Store Program -- # ------------- #

# Add short delays to simulate natural program response
import time


# Available items and their prices
menu = {
    "soda": 3.25,
    "fries": 6.35,
    "chips": 1.79,
    "pepsi": 2.81,
    "pizza": 4.56
}

cart = []
total_price = 0

# Separator used to organize the program output
divider = "#" + "-" * 50 + "#"


# Main shopping loop
while True:

    # Display the menu before each selection
    print("🛍 - Menu -")

    for item, value in menu.items():
        print(f"{item:5}: {value:.2f}$")

    print(divider)

    # Ask the user to choose an item
    food = input("- 🛒 Select an item (or q to quit): ").lower().strip()

    # Exit the application when the user enters q
    if food == "q":
        for dots in range(4):
            print(f'\r🚪 The app is closing{"." * dots}', end="", flush=True)
            time.sleep(0.4)

        print("\n👋 Thanks for using our App!")
        break

    # Check if the selected item exists in the menu
    if food in menu:
        price = menu[food]

        # Add the selected item to the cart
        cart.append(food)

        # Update the total price
        total_price += price

        # Convert cart items into a readable string
        cart_items = ", ".join(cart)
        
        # Simulating processing before adding the element
        print("\nProcessing...")
        time.sleep(0.5)
        
        # Show the result of the purchase
        print(f"✅ {food}: {price:.2f}$ has been added to your cart.")
        print(f"🧾 Cart: [{cart_items}]")
        print(f"💰 Total cost: {total_price:.2f}$")
        time.sleep(0.7)

    else:
        # Handle numbers as invalid input
        if food.isdigit():
            print("❌ Numbers aren't allowed!")

        # Handle items that are not available in the menu
        else:
            print(f"⚠️ Invalid item! '{food}' is not in the list.")

    # Small delay before the next interaction
    time.sleep(0.8)
    print(divider)


# ---------------------------------------------------- #