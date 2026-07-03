def pizza_order():
    print("\n🍕 Welcome to Python Pizza Deliveries!\n")

    print("📋 Pizza Menu")
    print("🍕 Small (S)  - ₹199")
    print("🍕 Medium (M) - ₹349")
    print("🍕 Large (L)  - ₹499")
    print("\nExtras:")
    print("🧀 Extra Cheese - ₹30")
    print("🍖 Pepperoni (Small) - ₹50")
    print("🍖 Pepperoni (Medium/Large) - ₹80")

    size = input("\nChoose pizza size (S/M/L): ").upper()
    pepperoni = input("Do you want pepperoni? (Y/N): ").upper()
    extra_cheese = input("Do you want extra cheese? (Y/N): ").upper()

    bill = 0

    # Pizza Size
    if size == "S":
        bill += 199

    elif size == "M":
        bill += 349

    elif size == "L":
        bill += 499

    else:
        print("\n❌ Invalid pizza size selected.")
        return

    # Pepperoni
    if pepperoni == "Y":
        if size == "S":
            bill += 50
        else:
            bill += 80

    # Extra Cheese
    if extra_cheese == "Y":
        bill += 30

    print("\n-----------------------------")
    print(f"💰 Total Bill: ₹{bill}")
    print("🍕 Thank you for ordering with Python Pizza Deliveries!")
    print("-----------------------------")