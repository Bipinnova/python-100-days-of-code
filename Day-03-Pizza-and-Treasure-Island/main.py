from pizza_order import pizza_order
from treasure_island import treasure_island


def main():

    while True:

        print("\n" + "=" * 50)
        print("🐍 Day 03 - Conditional Logic")
        print("=" * 50)

        print("\nChoose a project:")
        print("1. 🍕 Pizza Order")
        print("2. 🏝 Treasure Island")
        print("3. ❌ Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            pizza_order()

        elif choice == "2":
            treasure_island()

        elif choice == "3":
            print("\n👋 Thanks for trying today's projects!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")

        again = input("\nWould you like to run another project? (Y/N): ").upper()

        if again != "Y":
            print("\n👋 Thank you!")
            break



main()