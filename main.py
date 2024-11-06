from personal_info import PersonalInfoManager
import os
import json

class Main():
    def main():
        manager = PersonalInfoManager('data/personal_info.json')

        while True:
            print(" \n1. Add Info:\n2. View Info:\n3. Update Info:\n4. Delete Info:\n5. Exit")
            choice = input("Choose an option")

            if choice == '1':
                name = input("Enter name: ")
                age = input("Enter age: ")
                email = input("Enter email: ")
                address = input("Enter address: ")

                manager.add_info(name,age,email,address)
                print(f"Info for {name} added")
            elif choice == '2':
                info = manager.load_info()
                if info == True:
                    for name, details in info.items():
                        print(f"\nName: {name}")
                        print(f"Age: {details['age']}")
                        print(f"Email: {details['email']}")
                        print(f"Address: {details['address']}")
                else:
                   print("No information found.") 
            elif choice == '3':
                pass
            elif choice == '4':
                pass
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    if __name__ == '__main__':
        main()