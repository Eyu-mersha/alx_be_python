def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == '1':
            item= input("What is the item you want to add")
            shopping_list.append(item)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item= input("What is the item you want to remove")
            if shopping_list.__contains__(item):
                shopping_list.remove(item)
            else:
                print("Item not found in the list")    
            pass
        elif choice == '3':
            # Display the shopping list
            for i in shopping_list:
                print(i)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()